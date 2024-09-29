# Generated from antlr_generated/Lua.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,59,339,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,3,0,57,8,0,5,0,59,8,0,10,0,12,0,62,9,0,1,0,1,0,3,0,66,8,
        0,3,0,68,8,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,5,2,101,8,2,10,2,12,2,104,9,2,1,2,1,2,3,2,108,8,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,120,8,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,146,8,2,3,2,148,8,2,1,3,1,3,3,3,152,8,3,1,3,3,
        3,155,8,3,1,4,1,4,1,4,5,4,160,8,4,10,4,12,4,163,9,4,1,4,1,4,3,4,
        167,8,4,1,5,1,5,1,5,5,5,172,8,5,10,5,12,5,175,9,5,1,6,1,6,1,6,5,
        6,180,8,6,10,6,12,6,183,9,6,1,7,1,7,1,7,5,7,188,8,7,10,7,12,7,191,
        9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,
        207,8,8,1,8,1,8,1,8,5,8,212,8,8,10,8,12,8,215,9,8,1,9,1,9,1,9,1,
        9,1,9,1,9,3,9,223,8,9,1,9,5,9,226,8,9,10,9,12,9,229,9,9,1,10,1,10,
        5,10,233,8,10,10,10,12,10,236,9,10,1,11,1,11,4,11,240,8,11,11,11,
        12,11,241,1,12,1,12,1,12,1,12,1,12,3,12,249,8,12,1,13,1,13,3,13,
        253,8,13,1,13,1,13,1,14,5,14,258,8,14,10,14,12,14,261,9,14,1,14,
        1,14,1,14,1,14,1,14,1,14,3,14,269,8,14,1,15,1,15,3,15,273,8,15,1,
        15,1,15,1,15,3,15,278,8,15,1,16,1,16,1,16,1,17,1,17,3,17,285,8,17,
        1,17,1,17,1,17,1,17,1,18,1,18,1,18,3,18,294,8,18,1,18,3,18,297,8,
        18,1,19,1,19,3,19,301,8,19,1,19,1,19,1,20,1,20,1,20,1,20,5,20,309,
        8,20,10,20,12,20,312,9,20,1,20,3,20,315,8,20,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,3,21,327,8,21,1,22,1,22,1,23,1,23,
        1,24,1,24,1,25,1,25,1,26,1,26,1,26,0,0,27,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,0,5,2,0,1,
        1,13,13,1,0,31,45,2,0,32,32,46,47,1,0,49,52,1,0,53,55,365,0,60,1,
        0,0,0,2,69,1,0,0,0,4,147,1,0,0,0,6,154,1,0,0,0,8,156,1,0,0,0,10,
        168,1,0,0,0,12,176,1,0,0,0,14,189,1,0,0,0,16,206,1,0,0,0,18,222,
        1,0,0,0,20,230,1,0,0,0,22,237,1,0,0,0,24,248,1,0,0,0,26,252,1,0,
        0,0,28,259,1,0,0,0,30,277,1,0,0,0,32,279,1,0,0,0,34,282,1,0,0,0,
        36,296,1,0,0,0,38,298,1,0,0,0,40,304,1,0,0,0,42,326,1,0,0,0,44,328,
        1,0,0,0,46,330,1,0,0,0,48,332,1,0,0,0,50,334,1,0,0,0,52,336,1,0,
        0,0,54,56,3,4,2,0,55,57,5,1,0,0,56,55,1,0,0,0,56,57,1,0,0,0,57,59,
        1,0,0,0,58,54,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,
        61,67,1,0,0,0,62,60,1,0,0,0,63,65,3,6,3,0,64,66,5,1,0,0,65,64,1,
        0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,63,1,0,0,0,67,68,1,0,0,0,68,
        1,1,0,0,0,69,70,3,0,0,0,70,3,1,0,0,0,71,72,3,10,5,0,72,73,5,2,0,
        0,73,74,3,14,7,0,74,148,1,0,0,0,75,148,3,22,11,0,76,77,5,3,0,0,77,
        78,3,2,1,0,78,79,5,4,0,0,79,148,1,0,0,0,80,81,5,5,0,0,81,82,3,16,
        8,0,82,83,5,3,0,0,83,84,3,2,1,0,84,85,5,4,0,0,85,148,1,0,0,0,86,
        87,5,6,0,0,87,88,3,2,1,0,88,89,5,7,0,0,89,90,3,16,8,0,90,148,1,0,
        0,0,91,92,5,8,0,0,92,93,3,16,8,0,93,94,5,9,0,0,94,102,3,2,1,0,95,
        96,5,10,0,0,96,97,3,16,8,0,97,98,5,9,0,0,98,99,3,2,1,0,99,101,1,
        0,0,0,100,95,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,
        0,0,103,107,1,0,0,0,104,102,1,0,0,0,105,106,5,11,0,0,106,108,3,2,
        1,0,107,105,1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,110,5,4,
        0,0,110,148,1,0,0,0,111,112,5,12,0,0,112,113,5,48,0,0,113,114,5,
        2,0,0,114,115,3,16,8,0,115,116,5,13,0,0,116,119,3,16,8,0,117,118,
        5,13,0,0,118,120,3,16,8,0,119,117,1,0,0,0,119,120,1,0,0,0,120,121,
        1,0,0,0,121,122,5,3,0,0,122,123,3,2,1,0,123,124,5,4,0,0,124,148,
        1,0,0,0,125,126,5,12,0,0,126,127,3,12,6,0,127,128,5,14,0,0,128,129,
        3,14,7,0,129,130,5,3,0,0,130,131,3,2,1,0,131,132,5,4,0,0,132,148,
        1,0,0,0,133,134,5,15,0,0,134,135,3,8,4,0,135,136,3,34,17,0,136,148,
        1,0,0,0,137,138,5,16,0,0,138,139,5,15,0,0,139,140,5,48,0,0,140,148,
        3,34,17,0,141,142,5,16,0,0,142,145,3,12,6,0,143,144,5,2,0,0,144,
        146,3,14,7,0,145,143,1,0,0,0,145,146,1,0,0,0,146,148,1,0,0,0,147,
        71,1,0,0,0,147,75,1,0,0,0,147,76,1,0,0,0,147,80,1,0,0,0,147,86,1,
        0,0,0,147,91,1,0,0,0,147,111,1,0,0,0,147,125,1,0,0,0,147,133,1,0,
        0,0,147,137,1,0,0,0,147,141,1,0,0,0,148,5,1,0,0,0,149,151,5,17,0,
        0,150,152,3,14,7,0,151,150,1,0,0,0,151,152,1,0,0,0,152,155,1,0,0,
        0,153,155,5,18,0,0,154,149,1,0,0,0,154,153,1,0,0,0,155,7,1,0,0,0,
        156,161,5,48,0,0,157,158,5,19,0,0,158,160,5,48,0,0,159,157,1,0,0,
        0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,166,1,0,0,
        0,163,161,1,0,0,0,164,165,5,20,0,0,165,167,5,48,0,0,166,164,1,0,
        0,0,166,167,1,0,0,0,167,9,1,0,0,0,168,173,3,18,9,0,169,170,5,13,
        0,0,170,172,3,18,9,0,171,169,1,0,0,0,172,175,1,0,0,0,173,171,1,0,
        0,0,173,174,1,0,0,0,174,11,1,0,0,0,175,173,1,0,0,0,176,181,5,48,
        0,0,177,178,5,13,0,0,178,180,5,48,0,0,179,177,1,0,0,0,180,183,1,
        0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,13,1,0,0,0,183,181,1,0,
        0,0,184,185,3,16,8,0,185,186,5,13,0,0,186,188,1,0,0,0,187,184,1,
        0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,192,1,
        0,0,0,191,189,1,0,0,0,192,193,3,16,8,0,193,15,1,0,0,0,194,207,5,
        21,0,0,195,207,5,22,0,0,196,207,5,23,0,0,197,207,3,50,25,0,198,207,
        3,52,26,0,199,207,5,24,0,0,200,207,3,32,16,0,201,207,3,20,10,0,202,
        207,3,38,19,0,203,204,3,48,24,0,204,205,3,16,8,0,205,207,1,0,0,0,
        206,194,1,0,0,0,206,195,1,0,0,0,206,196,1,0,0,0,206,197,1,0,0,0,
        206,198,1,0,0,0,206,199,1,0,0,0,206,200,1,0,0,0,206,201,1,0,0,0,
        206,202,1,0,0,0,206,203,1,0,0,0,207,213,1,0,0,0,208,209,3,46,23,
        0,209,210,3,16,8,0,210,212,1,0,0,0,211,208,1,0,0,0,212,215,1,0,0,
        0,213,211,1,0,0,0,213,214,1,0,0,0,214,17,1,0,0,0,215,213,1,0,0,0,
        216,223,5,48,0,0,217,218,5,25,0,0,218,219,3,16,8,0,219,220,5,26,
        0,0,220,221,3,28,14,0,221,223,1,0,0,0,222,216,1,0,0,0,222,217,1,
        0,0,0,223,227,1,0,0,0,224,226,3,28,14,0,225,224,1,0,0,0,226,229,
        1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,19,1,0,0,0,229,227,1,
        0,0,0,230,234,3,24,12,0,231,233,3,26,13,0,232,231,1,0,0,0,233,236,
        1,0,0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,21,1,0,0,0,236,234,1,
        0,0,0,237,239,3,24,12,0,238,240,3,26,13,0,239,238,1,0,0,0,240,241,
        1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,23,1,0,0,0,243,249,3,
        18,9,0,244,245,5,25,0,0,245,246,3,16,8,0,246,247,5,26,0,0,247,249,
        1,0,0,0,248,243,1,0,0,0,248,244,1,0,0,0,249,25,1,0,0,0,250,251,5,
        20,0,0,251,253,5,48,0,0,252,250,1,0,0,0,252,253,1,0,0,0,253,254,
        1,0,0,0,254,255,3,30,15,0,255,27,1,0,0,0,256,258,3,26,13,0,257,256,
        1,0,0,0,258,261,1,0,0,0,259,257,1,0,0,0,259,260,1,0,0,0,260,268,
        1,0,0,0,261,259,1,0,0,0,262,263,5,27,0,0,263,264,3,16,8,0,264,265,
        5,28,0,0,265,269,1,0,0,0,266,267,5,19,0,0,267,269,5,48,0,0,268,262,
        1,0,0,0,268,266,1,0,0,0,269,29,1,0,0,0,270,272,5,25,0,0,271,273,
        3,14,7,0,272,271,1,0,0,0,272,273,1,0,0,0,273,274,1,0,0,0,274,278,
        5,26,0,0,275,278,3,38,19,0,276,278,3,52,26,0,277,270,1,0,0,0,277,
        275,1,0,0,0,277,276,1,0,0,0,278,31,1,0,0,0,279,280,5,15,0,0,280,
        281,3,34,17,0,281,33,1,0,0,0,282,284,5,25,0,0,283,285,3,36,18,0,
        284,283,1,0,0,0,284,285,1,0,0,0,285,286,1,0,0,0,286,287,5,26,0,0,
        287,288,3,2,1,0,288,289,5,4,0,0,289,35,1,0,0,0,290,293,3,12,6,0,
        291,292,5,13,0,0,292,294,5,24,0,0,293,291,1,0,0,0,293,294,1,0,0,
        0,294,297,1,0,0,0,295,297,5,24,0,0,296,290,1,0,0,0,296,295,1,0,0,
        0,297,37,1,0,0,0,298,300,5,29,0,0,299,301,3,40,20,0,300,299,1,0,
        0,0,300,301,1,0,0,0,301,302,1,0,0,0,302,303,5,30,0,0,303,39,1,0,
        0,0,304,310,3,42,21,0,305,306,3,44,22,0,306,307,3,42,21,0,307,309,
        1,0,0,0,308,305,1,0,0,0,309,312,1,0,0,0,310,308,1,0,0,0,310,311,
        1,0,0,0,311,314,1,0,0,0,312,310,1,0,0,0,313,315,3,44,22,0,314,313,
        1,0,0,0,314,315,1,0,0,0,315,41,1,0,0,0,316,317,5,27,0,0,317,318,
        3,16,8,0,318,319,5,28,0,0,319,320,5,2,0,0,320,321,3,16,8,0,321,327,
        1,0,0,0,322,323,5,48,0,0,323,324,5,2,0,0,324,327,3,16,8,0,325,327,
        3,16,8,0,326,316,1,0,0,0,326,322,1,0,0,0,326,325,1,0,0,0,327,43,
        1,0,0,0,328,329,7,0,0,0,329,45,1,0,0,0,330,331,7,1,0,0,331,47,1,
        0,0,0,332,333,7,2,0,0,333,49,1,0,0,0,334,335,7,3,0,0,335,51,1,0,
        0,0,336,337,7,4,0,0,337,53,1,0,0,0,35,56,60,65,67,102,107,119,145,
        147,151,154,161,166,173,181,189,206,213,222,227,234,241,248,252,
        259,268,272,277,284,293,296,300,310,314,326
    ]

class LuaParser ( Parser ):

    grammarFileName = "Lua.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'do'", "'end'", "'while'", 
                     "'repeat'", "'until'", "'if'", "'then'", "'elseif'", 
                     "'else'", "'for'", "','", "'in'", "'function'", "'local'", 
                     "'return'", "'break'", "'.'", "':'", "'nil'", "'false'", 
                     "'true'", "'...'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "'+'", "'-'", "'*'", "'/'", "'^'", "'%'", "'..'", 
                     "'<'", "'<='", "'>'", "'>='", "'=='", "'~='", "'and'", 
                     "'or'", "'not'", "'#'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NAME", "INT", "FLOAT", "EXP", "HEX", "NORMALSTRING", 
                      "CHARSTRING", "LONGSTRING", "COMMENT", "LINE_COMMENT", 
                      "WS", "NEWLINE" ]

    RULE_chunk = 0
    RULE_block = 1
    RULE_stat = 2
    RULE_laststat = 3
    RULE_funcname = 4
    RULE_varlist1 = 5
    RULE_namelist = 6
    RULE_explist1 = 7
    RULE_exp = 8
    RULE_var = 9
    RULE_prefixexp = 10
    RULE_functioncall = 11
    RULE_varOrExp = 12
    RULE_nameAndArgs = 13
    RULE_varSuffix = 14
    RULE_args = 15
    RULE_function = 16
    RULE_funcbody = 17
    RULE_parlist1 = 18
    RULE_tableconstructor = 19
    RULE_fieldlist = 20
    RULE_field = 21
    RULE_fieldsep = 22
    RULE_binop = 23
    RULE_unop = 24
    RULE_number = 25
    RULE_string = 26

    ruleNames =  [ "chunk", "block", "stat", "laststat", "funcname", "varlist1", 
                   "namelist", "explist1", "exp", "var", "prefixexp", "functioncall", 
                   "varOrExp", "nameAndArgs", "varSuffix", "args", "function", 
                   "funcbody", "parlist1", "tableconstructor", "fieldlist", 
                   "field", "fieldsep", "binop", "unop", "number", "string" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    NAME=48
    INT=49
    FLOAT=50
    EXP=51
    HEX=52
    NORMALSTRING=53
    CHARSTRING=54
    LONGSTRING=55
    COMMENT=56
    LINE_COMMENT=57
    WS=58
    NEWLINE=59

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ChunkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.StatContext)
            else:
                return self.getTypedRuleContext(LuaParser.StatContext,i)


        def laststat(self):
            return self.getTypedRuleContext(LuaParser.LaststatContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_chunk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChunk" ):
                listener.enterChunk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChunk" ):
                listener.exitChunk(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChunk" ):
                return visitor.visitChunk(self)
            else:
                return visitor.visitChildren(self)




    def chunk(self):

        localctx = LuaParser.ChunkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_chunk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 281475010367848) != 0):
                self.state = 54
                self.stat()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 55
                    self.match(LuaParser.T__0)


                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17 or _la==18:
                self.state = 63
                self.laststat()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 64
                    self.match(LuaParser.T__0)




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chunk(self):
            return self.getTypedRuleContext(LuaParser.ChunkContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = LuaParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.chunk()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varlist1(self):
            return self.getTypedRuleContext(LuaParser.Varlist1Context,0)


        def explist1(self):
            return self.getTypedRuleContext(LuaParser.Explist1Context,0)


        def functioncall(self):
            return self.getTypedRuleContext(LuaParser.FunctioncallContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.BlockContext)
            else:
                return self.getTypedRuleContext(LuaParser.BlockContext,i)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def namelist(self):
            return self.getTypedRuleContext(LuaParser.NamelistContext,0)


        def funcname(self):
            return self.getTypedRuleContext(LuaParser.FuncnameContext,0)


        def funcbody(self):
            return self.getTypedRuleContext(LuaParser.FuncbodyContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = LuaParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.varlist1()
                self.state = 72
                self.match(LuaParser.T__1)
                self.state = 73
                self.explist1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.functioncall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.match(LuaParser.T__2)
                self.state = 77
                self.block()
                self.state = 78
                self.match(LuaParser.T__3)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 80
                self.match(LuaParser.T__4)
                self.state = 81
                self.exp()
                self.state = 82
                self.match(LuaParser.T__2)
                self.state = 83
                self.block()
                self.state = 84
                self.match(LuaParser.T__3)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 86
                self.match(LuaParser.T__5)
                self.state = 87
                self.block()
                self.state = 88
                self.match(LuaParser.T__6)
                self.state = 89
                self.exp()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 91
                self.match(LuaParser.T__7)
                self.state = 92
                self.exp()
                self.state = 93
                self.match(LuaParser.T__8)
                self.state = 94
                self.block()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 95
                    self.match(LuaParser.T__9)
                    self.state = 96
                    self.exp()
                    self.state = 97
                    self.match(LuaParser.T__8)
                    self.state = 98
                    self.block()
                    self.state = 104
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 105
                    self.match(LuaParser.T__10)
                    self.state = 106
                    self.block()


                self.state = 109
                self.match(LuaParser.T__3)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 111
                self.match(LuaParser.T__11)
                self.state = 112
                self.match(LuaParser.NAME)
                self.state = 113
                self.match(LuaParser.T__1)
                self.state = 114
                self.exp()
                self.state = 115
                self.match(LuaParser.T__12)
                self.state = 116
                self.exp()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 117
                    self.match(LuaParser.T__12)
                    self.state = 118
                    self.exp()


                self.state = 121
                self.match(LuaParser.T__2)
                self.state = 122
                self.block()
                self.state = 123
                self.match(LuaParser.T__3)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 125
                self.match(LuaParser.T__11)
                self.state = 126
                self.namelist()
                self.state = 127
                self.match(LuaParser.T__13)
                self.state = 128
                self.explist1()
                self.state = 129
                self.match(LuaParser.T__2)
                self.state = 130
                self.block()
                self.state = 131
                self.match(LuaParser.T__3)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 133
                self.match(LuaParser.T__14)
                self.state = 134
                self.funcname()
                self.state = 135
                self.funcbody()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 137
                self.match(LuaParser.T__15)
                self.state = 138
                self.match(LuaParser.T__14)
                self.state = 139
                self.match(LuaParser.NAME)
                self.state = 140
                self.funcbody()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 141
                self.match(LuaParser.T__15)
                self.state = 142
                self.namelist()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 143
                    self.match(LuaParser.T__1)
                    self.state = 144
                    self.explist1()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LaststatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explist1(self):
            return self.getTypedRuleContext(LuaParser.Explist1Context,0)


        def getRuleIndex(self):
            return LuaParser.RULE_laststat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLaststat" ):
                listener.enterLaststat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLaststat" ):
                listener.exitLaststat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLaststat" ):
                return visitor.visitLaststat(self)
            else:
                return visitor.visitChildren(self)




    def laststat(self):

        localctx = LuaParser.LaststatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_laststat)
        self._la = 0 # Token type
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(LuaParser.T__16)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 71987230190632960) != 0):
                    self.state = 150
                    self.explist1()


                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.match(LuaParser.T__17)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.NAME)
            else:
                return self.getToken(LuaParser.NAME, i)

        def getRuleIndex(self):
            return LuaParser.RULE_funcname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncname" ):
                listener.enterFuncname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncname" ):
                listener.exitFuncname(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncname" ):
                return visitor.visitFuncname(self)
            else:
                return visitor.visitChildren(self)




    def funcname(self):

        localctx = LuaParser.FuncnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(LuaParser.NAME)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 157
                self.match(LuaParser.T__18)
                self.state = 158
                self.match(LuaParser.NAME)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 164
                self.match(LuaParser.T__19)
                self.state = 165
                self.match(LuaParser.NAME)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Varlist1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.VarContext)
            else:
                return self.getTypedRuleContext(LuaParser.VarContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_varlist1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarlist1" ):
                listener.enterVarlist1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarlist1" ):
                listener.exitVarlist1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarlist1" ):
                return visitor.visitVarlist1(self)
            else:
                return visitor.visitChildren(self)




    def varlist1(self):

        localctx = LuaParser.Varlist1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varlist1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.var()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 169
                self.match(LuaParser.T__12)
                self.state = 170
                self.var()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.NAME)
            else:
                return self.getToken(LuaParser.NAME, i)

        def getRuleIndex(self):
            return LuaParser.RULE_namelist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamelist" ):
                listener.enterNamelist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamelist" ):
                listener.exitNamelist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamelist" ):
                return visitor.visitNamelist(self)
            else:
                return visitor.visitChildren(self)




    def namelist(self):

        localctx = LuaParser.NamelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_namelist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(LuaParser.NAME)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 177
                    self.match(LuaParser.T__12)
                    self.state = 178
                    self.match(LuaParser.NAME) 
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explist1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_explist1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplist1" ):
                listener.enterExplist1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplist1" ):
                listener.exitExplist1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist1" ):
                return visitor.visitExplist1(self)
            else:
                return visitor.visitChildren(self)




    def explist1(self):

        localctx = LuaParser.Explist1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_explist1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 184
                    self.exp()
                    self.state = 185
                    self.match(LuaParser.T__12) 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 192
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(LuaParser.NumberContext,0)


        def string(self):
            return self.getTypedRuleContext(LuaParser.StringContext,0)


        def function(self):
            return self.getTypedRuleContext(LuaParser.FunctionContext,0)


        def prefixexp(self):
            return self.getTypedRuleContext(LuaParser.PrefixexpContext,0)


        def tableconstructor(self):
            return self.getTypedRuleContext(LuaParser.TableconstructorContext,0)


        def unop(self):
            return self.getTypedRuleContext(LuaParser.UnopContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def binop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.BinopContext)
            else:
                return self.getTypedRuleContext(LuaParser.BinopContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = LuaParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 194
                self.match(LuaParser.T__20)
                pass
            elif token in [22]:
                self.state = 195
                self.match(LuaParser.T__21)
                pass
            elif token in [23]:
                self.state = 196
                self.match(LuaParser.T__22)
                pass
            elif token in [49, 50, 51, 52]:
                self.state = 197
                self.number()
                pass
            elif token in [53, 54, 55]:
                self.state = 198
                self.string()
                pass
            elif token in [24]:
                self.state = 199
                self.match(LuaParser.T__23)
                pass
            elif token in [15]:
                self.state = 200
                self.function()
                pass
            elif token in [25, 48]:
                self.state = 201
                self.prefixexp()
                pass
            elif token in [29]:
                self.state = 202
                self.tableconstructor()
                pass
            elif token in [32, 46, 47]:
                self.state = 203
                self.unop()
                self.state = 204
                self.exp()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 208
                    self.binop()
                    self.state = 209
                    self.exp() 
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def varSuffix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.VarSuffixContext)
            else:
                return self.getTypedRuleContext(LuaParser.VarSuffixContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = LuaParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.state = 216
                self.match(LuaParser.NAME)
                pass
            elif token in [25]:
                self.state = 217
                self.match(LuaParser.T__24)
                self.state = 218
                self.exp()
                self.state = 219
                self.match(LuaParser.T__25)
                self.state = 220
                self.varSuffix()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 224
                    self.varSuffix() 
                self.state = 229
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrefixexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varOrExp(self):
            return self.getTypedRuleContext(LuaParser.VarOrExpContext,0)


        def nameAndArgs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.NameAndArgsContext)
            else:
                return self.getTypedRuleContext(LuaParser.NameAndArgsContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_prefixexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefixexp" ):
                listener.enterPrefixexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefixexp" ):
                listener.exitPrefixexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefixexp" ):
                return visitor.visitPrefixexp(self)
            else:
                return visitor.visitChildren(self)




    def prefixexp(self):

        localctx = LuaParser.PrefixexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_prefixexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.varOrExp()
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 231
                    self.nameAndArgs() 
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varOrExp(self):
            return self.getTypedRuleContext(LuaParser.VarOrExpContext,0)


        def nameAndArgs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.NameAndArgsContext)
            else:
                return self.getTypedRuleContext(LuaParser.NameAndArgsContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_functioncall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioncall" ):
                listener.enterFunctioncall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioncall" ):
                listener.exitFunctioncall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall" ):
                return visitor.visitFunctioncall(self)
            else:
                return visitor.visitChildren(self)




    def functioncall(self):

        localctx = LuaParser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functioncall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.varOrExp()
            self.state = 239 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 238
                    self.nameAndArgs()

                else:
                    raise NoViableAltException(self)
                self.state = 241 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarOrExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(LuaParser.VarContext,0)


        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_varOrExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarOrExp" ):
                listener.enterVarOrExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarOrExp" ):
                listener.exitVarOrExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarOrExp" ):
                return visitor.visitVarOrExp(self)
            else:
                return visitor.visitChildren(self)




    def varOrExp(self):

        localctx = LuaParser.VarOrExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_varOrExp)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(LuaParser.T__24)
                self.state = 245
                self.exp()
                self.state = 246
                self.match(LuaParser.T__25)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameAndArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def args(self):
            return self.getTypedRuleContext(LuaParser.ArgsContext,0)


        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_nameAndArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameAndArgs" ):
                listener.enterNameAndArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameAndArgs" ):
                listener.exitNameAndArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameAndArgs" ):
                return visitor.visitNameAndArgs(self)
            else:
                return visitor.visitChildren(self)




    def nameAndArgs(self):

        localctx = LuaParser.NameAndArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_nameAndArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 250
                self.match(LuaParser.T__19)
                self.state = 251
                self.match(LuaParser.NAME)


            self.state = 254
            self.args()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarSuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def nameAndArgs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.NameAndArgsContext)
            else:
                return self.getTypedRuleContext(LuaParser.NameAndArgsContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_varSuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarSuffix" ):
                listener.enterVarSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarSuffix" ):
                listener.exitVarSuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarSuffix" ):
                return visitor.visitVarSuffix(self)
            else:
                return visitor.visitChildren(self)




    def varSuffix(self):

        localctx = LuaParser.VarSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_varSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 63050395354660864) != 0):
                self.state = 256
                self.nameAndArgs()
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 262
                self.match(LuaParser.T__26)
                self.state = 263
                self.exp()
                self.state = 264
                self.match(LuaParser.T__27)
                pass
            elif token in [19]:
                self.state = 266
                self.match(LuaParser.T__18)
                self.state = 267
                self.match(LuaParser.NAME)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explist1(self):
            return self.getTypedRuleContext(LuaParser.Explist1Context,0)


        def tableconstructor(self):
            return self.getTypedRuleContext(LuaParser.TableconstructorContext,0)


        def string(self):
            return self.getTypedRuleContext(LuaParser.StringContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = LuaParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.match(LuaParser.T__24)
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 71987230190632960) != 0):
                    self.state = 271
                    self.explist1()


                self.state = 274
                self.match(LuaParser.T__25)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.tableconstructor()
                pass
            elif token in [53, 54, 55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 276
                self.string()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcbody(self):
            return self.getTypedRuleContext(LuaParser.FuncbodyContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = LuaParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(LuaParser.T__14)
            self.state = 280
            self.funcbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def parlist1(self):
            return self.getTypedRuleContext(LuaParser.Parlist1Context,0)


        def getRuleIndex(self):
            return LuaParser.RULE_funcbody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncbody" ):
                listener.enterFuncbody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncbody" ):
                listener.exitFuncbody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncbody" ):
                return visitor.visitFuncbody(self)
            else:
                return visitor.visitChildren(self)




    def funcbody(self):

        localctx = LuaParser.FuncbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funcbody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(LuaParser.T__24)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24 or _la==48:
                self.state = 283
                self.parlist1()


            self.state = 286
            self.match(LuaParser.T__25)
            self.state = 287
            self.block()
            self.state = 288
            self.match(LuaParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parlist1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namelist(self):
            return self.getTypedRuleContext(LuaParser.NamelistContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_parlist1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParlist1" ):
                listener.enterParlist1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParlist1" ):
                listener.exitParlist1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParlist1" ):
                return visitor.visitParlist1(self)
            else:
                return visitor.visitChildren(self)




    def parlist1(self):

        localctx = LuaParser.Parlist1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parlist1)
        self._la = 0 # Token type
        try:
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.namelist()
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 291
                    self.match(LuaParser.T__12)
                    self.state = 292
                    self.match(LuaParser.T__23)


                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(LuaParser.T__23)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableconstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldlist(self):
            return self.getTypedRuleContext(LuaParser.FieldlistContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_tableconstructor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableconstructor" ):
                listener.enterTableconstructor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableconstructor" ):
                listener.exitTableconstructor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableconstructor" ):
                return visitor.visitTableconstructor(self)
            else:
                return visitor.visitChildren(self)




    def tableconstructor(self):

        localctx = LuaParser.TableconstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_tableconstructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(LuaParser.T__28)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 71987230324850688) != 0):
                self.state = 299
                self.fieldlist()


            self.state = 302
            self.match(LuaParser.T__29)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.FieldContext)
            else:
                return self.getTypedRuleContext(LuaParser.FieldContext,i)


        def fieldsep(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.FieldsepContext)
            else:
                return self.getTypedRuleContext(LuaParser.FieldsepContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_fieldlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldlist" ):
                listener.enterFieldlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldlist" ):
                listener.exitFieldlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldlist" ):
                return visitor.visitFieldlist(self)
            else:
                return visitor.visitChildren(self)




    def fieldlist(self):

        localctx = LuaParser.FieldlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_fieldlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.field()
            self.state = 310
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 305
                    self.fieldsep()
                    self.state = 306
                    self.field() 
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==13:
                self.state = 313
                self.fieldsep()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = LuaParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_field)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(LuaParser.T__26)
                self.state = 317
                self.exp()
                self.state = 318
                self.match(LuaParser.T__27)
                self.state = 319
                self.match(LuaParser.T__1)
                self.state = 320
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.match(LuaParser.NAME)
                self.state = 323
                self.match(LuaParser.T__1)
                self.state = 324
                self.exp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 325
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldsepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_fieldsep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldsep" ):
                listener.enterFieldsep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldsep" ):
                listener.exitFieldsep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldsep" ):
                return visitor.visitFieldsep(self)
            else:
                return visitor.visitChildren(self)




    def fieldsep(self):

        localctx = LuaParser.FieldsepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_fieldsep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            _la = self._input.LA(1)
            if not(_la==1 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_binop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinop" ):
                listener.enterBinop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinop" ):
                listener.exitBinop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinop" ):
                return visitor.visitBinop(self)
            else:
                return visitor.visitChildren(self)




    def binop(self):

        localctx = LuaParser.BinopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_binop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 70366596694016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_unop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnop" ):
                listener.enterUnop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnop" ):
                listener.exitUnop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnop" ):
                return visitor.visitUnop(self)
            else:
                return visitor.visitChildren(self)




    def unop(self):

        localctx = LuaParser.UnopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_unop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 211110527500288) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LuaParser.INT, 0)

        def FLOAT(self):
            return self.getToken(LuaParser.FLOAT, 0)

        def EXP(self):
            return self.getToken(LuaParser.EXP, 0)

        def HEX(self):
            return self.getToken(LuaParser.HEX, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = LuaParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8444249301319680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMALSTRING(self):
            return self.getToken(LuaParser.NORMALSTRING, 0)

        def CHARSTRING(self):
            return self.getToken(LuaParser.CHARSTRING, 0)

        def LONGSTRING(self):
            return self.getToken(LuaParser.LONGSTRING, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = LuaParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 63050394783186944) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





