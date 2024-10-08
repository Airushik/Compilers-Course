from antlr4 import *
import llvmlite.ir as ir

from antlr_generated.LuaVisitor import LuaVisitor
from antlr_generated.LuaLexer import LuaLexer
from antlr_generated.LuaParser import LuaParser

#from code_generator.types import LuaTypes
from code_generator.symbol_table import SymbolTable, RedefinitionError
from code_generator.util import *
from code_generator.errors import *
from code_generator.types import LuaTypes


# класс-наследник, внутри которого переопределяются некоторые методы класса LuaVisitor;
# LuaVisitor был автоматически создан с помощью ANTLR4 для файла LuaVisitor.g4
class LuaGenerator(LuaVisitor):
    BASE_TYPE = 0
    ARRAY_TYPE = 1
    FUNCTION_TYPE = 2

    def __init__(self, error_listener=LuaErrorListener()):
        self.module = ir.Module()
        llvm_function = ir.Function(self.module, ir.FunctionType(ir.IntType(32), []), name="main")
        self.builder = ir.IRBuilder(llvm_function.append_basic_block(name="main"))
        self.symbol_table = SymbolTable()

        self.continue_block = None
        self.break_block = None
        self.switch_context = None

        self.current_base_type = None
        self.is_global = True

        self.error_listener = error_listener
        self.global_context = ir.global_context
        self.struct_reflection = {}
        self.is_defining_struct = ''
    
    def visitStat(self, ctx: LuaParser.StatContext):
        print('Stat')
        print('vars available', self.symbol_table.names())
        
        #если присвоение глобальной переменной
        if match_rule(ctx.children[0], LuaParser.RULE_varlist1):
            # посещение правила varlist1
            lhs_ptr, name = self.visit(ctx.varlist1())
            print('name', name, type(name))
            
            # посещение правила explist
            explist = self.visit(ctx.explist1())
            rhs, rhs_type = explist[0]

            if lhs_ptr is None or lhs_ptr.type.pointee != rhs_type: #some wierd stuff!!
                self.symbol_table[name] = self.builder.alloca(rhs_type)
                lhs_ptr = self.symbol_table[name]
                converted_rhs = rhs
            else:
                converted_rhs = LuaTypes.cast_type(self.builder, value=rhs, target_type=lhs_ptr.type.pointee, ctx=ctx)
            
            print('stat store', converted_rhs.type, 'lhs_ptr', lhs_ptr.type)
            self.builder.store(value=converted_rhs, ptr=lhs_ptr)
            #return converted_rhs, None
        
        #если у нас if - else
        elif ctx.children[0].getText() == 'if':
            blocks = ctx.block()
            exps = ctx.exp()

            cond_val, _ = self.visit(exps[0])
            converted_cond_val = LuaTypes.cast_type(self.builder, target_type=LuaTypes.bool, value=cond_val, ctx=ctx)
            
            if ctx.children[-2].getText() == 'else':
                with self.builder.if_else(converted_cond_val) as (then, otherwise):
                    with then:
                        self.symbol_table.enter_scope()
                        self.visit(blocks[0])
                        self.symbol_table.exit_scope()
                    with otherwise:
                        self.symbol_table.enter_scope()
                        self.visit(blocks[-1])
                        self.symbol_table.exit_scope()
            else:
                with self.builder.if_then(converted_cond_val):
                    self.symbol_table.enter_scope()
                    self.visit(blocks[0])
                    self.symbol_table.exit_scope()
        #если while
        elif ctx.children[0].getText() == 'while':
            self.symbol_table.enter_scope()
            name_prefix = self.builder.block.name

            cond_block = self.builder.append_basic_block(name=name_prefix+".loop_cond")
            loop_block = self.builder.append_basic_block(name=name_prefix+".loop_body")
            end_block = self.builder.append_basic_block(name=name_prefix+".loop_end")

            last_break = self.break_block
            self.break_block = end_block

            self.builder.branch(cond_block)
            self.builder.position_at_start(cond_block)

            if ctx.exp() is not None and len(ctx.exp()) > 0:
                cond_val, _ = self.visit(ctx.exp()[0])
                converted_cond_val = LuaTypes.cast_type(self.builder, target_type=LuaTypes.bool, value=cond_val, ctx=ctx)
                self.builder.cbranch(converted_cond_val, loop_block, end_block)
            else:
                self.builder.branch(loop_block)

            self.builder.position_at_start(loop_block)
            self.visit(ctx.block()[0])
            self.builder.branch(cond_block)

            self.builder.position_at_start(end_block)
            self.break_block = last_break
            self.symbol_table.exit_scope()

        #если repeat
        elif ctx.children[0].getText() == 'repeat':
            self.symbol_table.enter_scope()
            name_prefix = self.builder.block.name

            cond_block = self.builder.append_basic_block(name=name_prefix+".loop_cond")
            loop_block = self.builder.append_basic_block(name=name_prefix+".loop_body")
            end_block = self.builder.append_basic_block(name=name_prefix+".loop_end")
            
            last_break = self.break_block
            self.break_block = end_block

            self.builder.branch(loop_block)
            self.builder.position_at_start(loop_block)
            self.visit(ctx.block()[0])

            self.builder.branch(cond_block)
            self.builder.position_at_start(cond_block)

            if ctx.exp() is not None and len(ctx.exp()) > 0:
                cond_val, _ = self.visit(ctx.exp()[0])
                converted_cond_val = LuaTypes.cast_type(self.builder, target_type=LuaTypes.bool, value=cond_val, ctx=ctx)
                self.builder.cbranch(converted_cond_val, loop_block, end_block)
            else:
                self.builder.branch(loop_block)

            self.builder.position_at_start(end_block)
            self.break_block = last_break
            self.symbol_table.exit_scope()
        
        #если for с сцетчиком
        elif ctx.children[0].getText() == 'for' and ctx.exp() is not None and len(ctx.exp()) > 0:
            self.symbol_table.enter_scope()
            name_prefix = self.builder.block.name

            cond_block = self.builder.append_basic_block(name=name_prefix+".loop_cond")
            loop_block = self.builder.append_basic_block(name=name_prefix+".loop_body")
            end_block = self.builder.append_basic_block(name=name_prefix+".loop_end")
            update_block = self.builder.append_basic_block(name=name_prefix+".loop_update")

            last_break = self.break_block
            self.break_block = end_block

            if ctx.NAME() is not None:
                name = ctx.NAME().getText()
            self.symbol_table[name] = self.builder.alloca(ir.IntType(32))
            counter = self.symbol_table[name]

            start_counter, _ = self.visit(ctx.exp()[0])
            self.builder.store(value=start_counter, ptr=counter)

            stop_counter, _ = self.visit(ctx.exp()[1])
            if len(ctx.exp()) > 2:
                step, _ = self.visit(ctx.exp()[2])
            else:
                step = ir.Constant(ir.IntType(32), 1)
            self.builder.branch(cond_block)

            self.builder.position_at_start(cond_block)
            counter_val = self.builder.load(counter)
            cond_val = self.builder.icmp_signed(cmpop='>', lhs=counter_val, rhs=stop_counter)
            converted_cond_val = LuaTypes.cast_type(self.builder, target_type=LuaTypes.bool, value=cond_val, ctx=ctx)
            self.builder.cbranch(converted_cond_val, loop_block, end_block)
            
            self.builder.position_at_start(loop_block)
            self.visit(ctx.block()[0])
            self.builder.branch(update_block)

            self.builder.position_at_start(update_block)
            if LuaTypes.is_int(counter_val.type) and LuaTypes.is_int(step.type):
                new_i = self.builder.add(counter_val, step)
                self.builder.store(value=new_i, ptr=counter)
            else:
                raise(SemanticError('Not int counter', ctx=ctx))
            self.builder.branch(cond_block)

            self.builder.position_at_start(end_block)
            self.break_block = last_break
            self.symbol_table.exit_scope()
        
        #если for без сцетчика (редкая ебень)
        elif ctx.children[0].getText() == 'for' and ctx.exp() is not None and len(ctx.exp()) > 0:
            #to do
            pass
        
        #если объявление функции 
        elif ctx.children[0].getText() == 'function':
            func_name = self.visit(ctx.funcname())
            params, funcblock = self.visit(ctx.funcbody())
            print('PARAMS', params)
            if params is not None:
                vars = self.visit(params)
            else:
                vars = []

            higher_builder = self.builder
            name_prefix = self.builder.block.name

            #содзаем временный билдер для временной функции, так как еще не знаем возвращаемый тип 
            temp_function = ir.Function(ir.Module(name=func_name), ir.FunctionType(ir.IntType(32), [ir.IntType(32) for i in range(len(vars))]), name=func_name)
            self.builder = ir.IRBuilder(temp_function.append_basic_block(name=name_prefix + '.' + func_name))
            self.symbol_table.enter_scope()

            old_breack_block = self.break_block
            self.break_block = None
            print('args', vars, temp_function.args)
            for arg_name, llvm_arg in zip(vars, temp_function.args):
                self.symbol_table[arg_name] = self.builder.alloca(llvm_arg.type)
                self.builder.store(llvm_arg, self.symbol_table[arg_name])

            #луа сохраняет значения внешних локальных переменных как константы
            #в момент объявления функций sic!
            #но пусть об этом подумает будущая я
            #for name in self.symbol_table.names():
            #    print('vars', name)
            #    if name not in vars:
            #        var = self.symbol_table[name]
            #        new_var = self.builder.alloca(var.type)
            #        self.symbol_table[name] = new_var
            #        val = self.builder.load(var)
            #        self.builder.store(new_var, val)
            #        print('vars in func', name, val)
        
            ret_type = self.visit(funcblock)
            
            real_function = ir.Function(self.module, ir.FunctionType(ret_type, [ir.IntType(32) for i in range(len(vars))]), name=func_name)
            real_function.blocks = temp_function.blocks

            self.symbol_table.set_global(func_name, real_function)

            self.break_block = old_breack_block
            self.builder = higher_builder

            self.symbol_table.exit_scope()
        
        #если вызов функции
        elif match_rule(ctx.children[0], LuaParser.RULE_functioncall):
            self.visit(ctx.functioncall())

    def visitFuncname(self, ctx: LuaParser.FuncnameContext):
        name = ctx.NAME()[0].getText()
        return name
    
    def visitFuncbody(self, ctx: LuaParser.FuncbodyContext):
        return ctx.parlist1(), ctx.funcblock()

    def visitParlist1(self, ctx: LuaParser.Parlist1Context):
        
        if ctx.namelist() is not None:
            names = self.visit(ctx.namelist())
        print('namelist in params!!!!!!!!!!!!!', names)
        return names
    
    def visitNamelist(self, ctx: LuaParser.NamelistContext):
        names_nodes = ctx.NAME()
        names = list()
        print('len names noooooooodeds',len(names_nodes))
        for node in names_nodes:
            names.append(node.getText())
        return names 

    def visitLaststat(self, ctx: LuaParser.LaststatContext):
        if ctx.children[0].getText() == 'break':
            if self.break_block is None:
                raise SemanticError(msg="Break can not be used here!", ctx=ctx)
            self.builder.branch(self.break_block)
        elif ctx.children[0].getText() == 'return':
            exps = self.visit(ctx.explist1())
            exp_val, exp_type = exps[0]
            self.builder.ret(exp_val)
            return exp_type
        
    def visitFuncchunk(self, ctx: LuaParser.FuncchunkContext):
        for child in ctx.stat():
            self.visit(child)
        if ctx.laststat() is not None:
            ret_type = self.visit(ctx.laststat())
            return ret_type
        else:
            self.builder.ret_void()
            return ir.VoidType()
        
    def visitFuncblock(self, ctx: LuaParser.FuncblockContext):
        if ctx.funcchunk() is not None:
            ret_type = self.visit(ctx.funcchunk())
            return ret_type
        return ret_type

    def visitVarlist1(self, ctx: LuaParser.Varlist1Context):
        #to do
        var, name = self.visit(ctx.var(0))
        return var, name
    
    def visitVar(self, ctx: LuaParser.VarContext):
        if ctx.NAME() is not None:
            name = ctx.NAME().getText()
            var = None
            print(self.symbol_table.names())
            if name in self.symbol_table:
                var = self.symbol_table[name]
            return var, name
    
    def visitExplist1(self, ctx: LuaParser.Explist1Context):
        print(len(ctx.exp()))
        exps = ctx.exp()
        exp_list = []
        for exp in exps:
            exp_val, exp_type = self.visit(ctx.exp()[0])
            exp_list.append((exp_val, exp_type))
        return exp_list
    
    def visitExp(self, ctx: LuaParser.ExpContext):
        print('2342342342',ctx.children[0].getText())
        if ctx.prefixexp() is not None:
            val, type = self.visit(ctx.prefixexp())
        elif ctx.tableconstructor() is not None:
            pass   #to do
        elif ctx.unop() is not None:
            unop = self.visit(ctx.unop())
            val, type = self.visit(ctx.exp(0))
            if unop == '-':
                val = self.builder.neg(val)
                type = val.type
            elif unop == 'not':
                val = self.builder.neg(val)
                type = val.type
            elif unop == '#':
                raise NotImplementedError("# is not implemented yet..")
        elif ctx.number() is not None:
            val, type = self.visit(ctx.number())
        elif ctx.string() is not None:
            val, type = self.visit(ctx.string())
        elif ctx.children[0].getText() is not None:
            text = ctx.children[0].getText()
            if text == 'nil':
                val = None #to do
                type = ir.VoidType()
            elif text == 'true':
                val = ir.Constant(ir.IntType(1), 1)
                type = val.type
            elif text == 'false':
                val = ir.Constant(ir.IntType(1), 0)
                type = val.type
        if ctx.binop() is not None and len(ctx.binop())!=0:
            print('binop!')
            exps = ctx.exp()
            binops = ctx.binop()
            print(len(ctx.binop()))
            if ctx.unop() is not None:
                start_i = 1
            else:
                start_i = 0
            for i in range(len(binops)):
                op = self.visit(ctx.binop(i))
                print(start_i + i, 'ind')
                binop_val, binop_type = self.visit(exps[start_i + i])
                binop_converted = LuaTypes.cast_type(self.builder, value=binop_val, target_type=type, ctx=ctx)

                if op == '+':
                    print('plus!')
                    print(val, binop_converted," !!!!!@!@!" )
                    if LuaTypes.is_int(type):
                        val = self.builder.add(val, binop_converted)
                        type = val.type
                    else:
                        val = self.builder.fadd(val, binop_converted)
                        type = val.type
                elif op == '-':
                    if LuaTypes.is_int(type):
                        val = self.builder.sub(val, binop_converted)
                        type = val.type
                    else:
                        val = self.builder.fsub(val, binop_converted)
                        type = val.type
                elif op == '*':
                    if LuaTypes.is_int(type):
                        val = self.builder.mul(val, binop_converted)
                        type = val.type
                    else:
                        val = self.builder.fmul(val, binop_converted)
                        type = val.type
                elif op == '/':
                    if LuaTypes.is_int(type):
                        val = self.builder.sdiv(val, binop_converted)
                        type = val.type
                    else:
                        val = self.builder.fdiv(val, binop_converted)
                        type = val.type
                elif op == '%':
                    if LuaTypes.is_int(type):
                        val = self.builder.srem(val, binop_converted)
                        type = val.type
                    else:
                        raise SemanticError(msg="Float doesn't support % operation", ctx=ctx)
                elif op == 'and':
                    if LuaTypes.is_int():
                        val = self.builder.mul(val, binop_converted)
                        type = val.type
                elif op == 'or':
                    if LuaTypes.is_int():
                        val = self.builder.add(val, binop_converted)
                        type = val.type
                elif op in [ '<', '<=', '>', '>=', '==', '~=' ]:
                    op.replace('!', '~')
                    if LuaTypes.is_int(type):
                        val = self.builder.icmp_signed(cmpop=op, lhs=val, rhs=binop_converted)
                        type = val.type
                    elif LuaTypes.is_float(type):
                        val = self.builder.fcmp_ordered(cmpop=op, lhs=val, rhs=binop_converted)
                        print('fcmp',val)
                        type = val.type
            
        return val, type

    def visitPrefixexp(self, ctx: LuaParser.PrefixexpContext):
        val, type = self.visit(ctx.varOrExp())
        return val, type

    def visitFunctioncall(self, ctx: LuaParser.FunctioncallContext):
        function, _ = self.visit(ctx.varOrExp())
        args = self.visit(ctx.nameAndArgs()[0])
        converted_args = [LuaTypes.cast_type(self.builder, value=arg[0], target_type=ir.IntType(32), ctx=ctx)
                                  for arg in args]
        self.builder.call(function, converted_args)

    def visitNameAndArgs(self, ctx: LuaParser.NameAndArgsContext):
        args = self.visitArgs(ctx.args())
        return args
    
    def visitArgs(self, ctx: LuaParser.ArgsContext):
        if ctx.explist1() is not None:
            args = self.visit(ctx.explist1())
        return args

    def visitVarOrExp(self, ctx: LuaParser.VarOrExpContext):
        if ctx.var() is not None:
            var, _ = self.visit(ctx.var())
            print('varorexp!!!!!!!!!!!!!!', var)
            if hasattr(var, 'return_type'):
                val = var
            else:
                val = self.builder.load(var)
            type = val.type
        if ctx.exp() is not None:
            val, type = self.visit(ctx.exp())
        return val, type
    
    def visitNumber(self, ctx: LuaParser.NumberContext):
        print('number!')
        if ctx.INT() is not None:
            val = ctx.INT().getText() 
            const_value = LuaTypes.get_const_from_str(cls=LuaTypes, luatype=LuaTypes.int, const_value=val, ctx=ctx)
        if ctx.FLOAT() is not None:
            val = ctx.FLOAT().getText() 
            const_value = LuaTypes.get_const_from_str(cls=LuaTypes, luatype=LuaTypes.float, const_value=val, ctx=ctx)
        if ctx.EXP() is not None:
            val = ctx.EXP().getText() 
            print('EXP', val)
            const_value = LuaTypes.get_const_from_str(cls=LuaTypes, luatype=LuaTypes.float, const_value=val, ctx=ctx)
        return const_value, const_value.type

    def visitString(self, ctx: LuaParser.StringContext):
        print(ctx.getText())
        str = ctx.getText()
        const_value = LuaTypes.get_const_from_str(cls=LuaTypes, luatype=ir.ArrayType(LuaTypes.char, len(str)+1), const_value=str, ctx=ctx)
        return const_value, const_value.type

    def visitBinop(self, ctx: LuaParser.BinopContext):
        return ctx.getText()
    
    def visitUnop(self, ctx: LuaParser.BinopContext):
        return ctx.getText()

    def save(self, filename):
        self.builder.ret(ir.Constant(ir.IntType(32), 0))
        with open(filename, "w") as f:
            f.write(repr(self.module))   # записываем в файл строковое представление объекта self.module

# генерация LLVM IR для соответствующего Lua-файла
def generate_ir(input_filename, output_filename):
    lexer = LuaLexer(FileStream(input_filename))
    stream = CommonTokenStream(lexer)
    parser = LuaParser(stream)

    error_listener = LuaErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.block()

    generator = LuaGenerator(error_listener)
    generator.visit(tree)
    generator.save(output_filename)

    if len(error_listener.errors) == 0:
        return True
    else:
        error_listener.print_errors()
        return False
