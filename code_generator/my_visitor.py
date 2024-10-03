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
    
    #def visitBlock(self, ctx: LuaParser.BlockContext):
    #    print('Hi')
    #    print(ctx.children)
    #    return super().visitBlock(ctx)
    
    #def visitChunk(self, ctx: LuaParser.ChunkContext):
    #    self.visit(ctx.stat)

    #def visitLaststat(self, ctx: LuaParser.LaststatContext):
    #    print('last')
    #    return super().visitLaststat(ctx)
    
    def visitStat(self, ctx: LuaParser.StatContext):
        print('Stat')
        if match_rule(ctx.children[0], LuaParser.RULE_varlist1):
            # посещение правила varlist1
            lhs, lhs_ptr, name = self.visit(ctx.varlist1())
            print('name', name, type(name))
            
            # посещение правила explist
            rhs, rhs_type = self.visit(ctx.explist1())
            print('rhd', rhs, rhs_type, type(rhs))
            
            if lhs_ptr is None:
                self.symbol_table[name] = self.builder.alloca(rhs_type)
                lhs_ptr = self.symbol_table[name]
            
            converted_rhs = LuaTypes.cast_type(self.builder, value=rhs, target_type=lhs_ptr.type.pointee, ctx=ctx)
            
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
        
    def visitVarlist1(self, ctx: LuaParser.Varlist1Context):
        var_val, var, name = self.visit(ctx.var(0))
        return var_val, var, name
    
    def visitVar(self, ctx: LuaParser.VarContext):
        if hasattr(ctx, 'NAME'):
            name = ctx.NAME().getText()
            var_val = None
            var = None
            if name in self.symbol_table:
                var = self.symbol_table[name]
                var_val = self.builder.load(var)
            return var_val, var, name
    
    def visitExplist1(self, ctx: LuaParser.Explist1Context):
        exp_val, exp_type = self.visit(ctx.exp(0))
        return exp_val, exp_type
    
    def visitExp(self, ctx: LuaParser.ExpContext):
        if ctx.number() is not None:
            val, type = self.visit(ctx.number())
        elif ctx.string() is not None:
            val, type = self.visit(ctx.string())
        elif ctx.prefixexp() is not None:
            val, type = self.visit(ctx.prefixexp())
        elif ctx.getText() is not None:
            text = ctx.getText()
            print('TEXT!', text)
            if text == 'nil':
                val = None
                type = ir.VoidType()
            elif text == 'true':
                val = ir.Constant(ir.IntType(1), 1)
                type = val.type
            elif text == 'false':
                val = ir.Constant(ir.IntType(1), 0)
                type = val.type
            
        elif ctx.tableconstructor() is not None:
            val, type = self.visit(ctx.string())
        return val, type

    def visitPrefixexp(self, ctx: LuaParser.PrefixexpContext):
        val, type = self.visit(ctx.varOrExp())
        return val, type

    def visitVarOrExp(self, ctx: LuaParser.VarOrExpContext):
        if ctx.var() is not None:
            val, var, _ = self.visit(ctx.var())
            type = var.type
        if ctx.exp() is not None:
            val, type = self.visit(ctx.exp())
        return val, type
    
    def visitNumber(self, ctx: LuaParser.NumberContext):
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
        return const_value, const_value.type#val, type

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
