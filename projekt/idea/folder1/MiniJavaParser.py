# Generated from MiniJava.g4 by ANTLR 4.11.1
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
        4,1,48,212,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,0,1,0,5,0,25,8,0,10,0,12,0,28,
        9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,48,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,56,8,2,1,2,1,
        2,1,2,1,2,1,2,1,2,5,2,64,8,2,10,2,12,2,67,9,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,101,8,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,115,8,3,10,3,12,3,
        118,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,3,4,154,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,181,8,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,189,8,6,1,7,1,7,1,7,1,7,
        1,7,1,7,3,7,197,8,7,1,7,1,7,1,7,1,7,1,7,3,7,204,8,7,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,0,2,4,6,9,0,2,4,6,8,10,12,14,16,0,3,3,0,43,43,46,
        46,48,48,1,0,34,36,1,0,32,33,240,0,26,1,0,0,0,2,47,1,0,0,0,4,55,
        1,0,0,0,6,100,1,0,0,0,8,153,1,0,0,0,10,180,1,0,0,0,12,182,1,0,0,
        0,14,203,1,0,0,0,16,205,1,0,0,0,18,25,3,4,2,0,19,25,3,8,4,0,20,25,
        3,6,3,0,21,25,3,10,5,0,22,25,3,12,6,0,23,25,3,2,1,0,24,18,1,0,0,
        0,24,19,1,0,0,0,24,20,1,0,0,0,24,21,1,0,0,0,24,22,1,0,0,0,24,23,
        1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,1,1,0,0,0,28,
        26,1,0,0,0,29,30,5,48,0,0,30,31,5,19,0,0,31,32,3,6,3,0,32,33,5,16,
        0,0,33,48,1,0,0,0,34,35,5,48,0,0,35,36,5,19,0,0,36,37,3,4,2,0,37,
        38,5,16,0,0,38,48,1,0,0,0,39,40,5,48,0,0,40,41,5,19,0,0,41,42,5,
        44,0,0,42,48,5,16,0,0,43,44,5,48,0,0,44,45,5,19,0,0,45,46,5,47,0,
        0,46,48,5,16,0,0,47,29,1,0,0,0,47,34,1,0,0,0,47,39,1,0,0,0,47,43,
        1,0,0,0,48,3,1,0,0,0,49,50,6,2,-1,0,50,51,5,10,0,0,51,52,3,4,2,0,
        52,53,5,11,0,0,53,56,1,0,0,0,54,56,7,0,0,0,55,49,1,0,0,0,55,54,1,
        0,0,0,56,65,1,0,0,0,57,58,10,4,0,0,58,59,7,1,0,0,59,64,3,4,2,5,60,
        61,10,3,0,0,61,62,7,2,0,0,62,64,3,4,2,4,63,57,1,0,0,0,63,60,1,0,
        0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,5,1,0,0,0,67,65,
        1,0,0,0,68,69,6,3,-1,0,69,70,3,4,2,0,70,71,5,24,0,0,71,72,3,4,2,
        0,72,101,1,0,0,0,73,74,3,4,2,0,74,75,5,27,0,0,75,76,3,4,2,0,76,101,
        1,0,0,0,77,78,3,4,2,0,78,79,5,21,0,0,79,80,3,4,2,0,80,101,1,0,0,
        0,81,82,3,4,2,0,82,83,5,25,0,0,83,84,3,4,2,0,84,101,1,0,0,0,85,86,
        3,4,2,0,86,87,5,20,0,0,87,88,3,4,2,0,88,101,1,0,0,0,89,90,3,4,2,
        0,90,91,5,26,0,0,91,92,3,4,2,0,92,101,1,0,0,0,93,94,5,22,0,0,94,
        101,3,6,3,3,95,96,5,10,0,0,96,97,3,6,3,0,97,98,5,11,0,0,98,101,1,
        0,0,0,99,101,5,45,0,0,100,68,1,0,0,0,100,73,1,0,0,0,100,77,1,0,0,
        0,100,81,1,0,0,0,100,85,1,0,0,0,100,89,1,0,0,0,100,93,1,0,0,0,100,
        95,1,0,0,0,100,99,1,0,0,0,101,116,1,0,0,0,102,103,10,13,0,0,103,
        104,5,28,0,0,104,115,3,6,3,14,105,106,10,12,0,0,106,107,5,29,0,0,
        107,115,3,6,3,13,108,109,10,11,0,0,109,110,5,24,0,0,110,115,3,6,
        3,12,111,112,10,10,0,0,112,113,5,27,0,0,113,115,3,6,3,11,114,102,
        1,0,0,0,114,105,1,0,0,0,114,108,1,0,0,0,114,111,1,0,0,0,115,118,
        1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,7,1,0,0,0,118,116,1,
        0,0,0,119,120,5,1,0,0,120,121,3,6,3,0,121,122,5,11,0,0,122,123,5,
        16,0,0,123,154,1,0,0,0,124,125,5,1,0,0,125,126,5,44,0,0,126,127,
        5,11,0,0,127,154,5,16,0,0,128,129,5,1,0,0,129,130,5,43,0,0,130,131,
        5,11,0,0,131,154,5,16,0,0,132,133,5,1,0,0,133,134,5,46,0,0,134,135,
        5,11,0,0,135,154,5,16,0,0,136,137,5,1,0,0,137,138,5,45,0,0,138,139,
        5,11,0,0,139,154,5,16,0,0,140,141,5,1,0,0,141,142,5,47,0,0,142,143,
        5,11,0,0,143,154,5,16,0,0,144,145,5,1,0,0,145,146,5,48,0,0,146,147,
        5,11,0,0,147,154,5,16,0,0,148,149,5,1,0,0,149,150,3,4,2,0,150,151,
        5,11,0,0,151,152,5,16,0,0,152,154,1,0,0,0,153,119,1,0,0,0,153,124,
        1,0,0,0,153,128,1,0,0,0,153,132,1,0,0,0,153,136,1,0,0,0,153,140,
        1,0,0,0,153,144,1,0,0,0,153,148,1,0,0,0,154,9,1,0,0,0,155,156,5,
        2,0,0,156,157,5,48,0,0,157,158,5,19,0,0,158,159,5,43,0,0,159,181,
        5,16,0,0,160,161,5,3,0,0,161,162,5,48,0,0,162,163,5,19,0,0,163,164,
        5,47,0,0,164,181,5,16,0,0,165,166,5,4,0,0,166,167,5,48,0,0,167,168,
        5,19,0,0,168,169,5,44,0,0,169,181,5,16,0,0,170,171,5,5,0,0,171,172,
        5,48,0,0,172,173,5,19,0,0,173,174,5,46,0,0,174,181,5,16,0,0,175,
        176,5,6,0,0,176,177,5,48,0,0,177,178,5,19,0,0,178,179,5,45,0,0,179,
        181,5,16,0,0,180,155,1,0,0,0,180,160,1,0,0,0,180,165,1,0,0,0,180,
        170,1,0,0,0,180,175,1,0,0,0,181,11,1,0,0,0,182,183,5,41,0,0,183,
        184,3,6,3,0,184,185,5,12,0,0,185,186,3,0,0,0,186,188,5,13,0,0,187,
        189,3,14,7,0,188,187,1,0,0,0,188,189,1,0,0,0,189,13,1,0,0,0,190,
        191,5,7,0,0,191,192,3,6,3,0,192,193,5,12,0,0,193,194,3,0,0,0,194,
        196,5,13,0,0,195,197,3,14,7,0,196,195,1,0,0,0,196,197,1,0,0,0,197,
        204,1,0,0,0,198,199,5,8,0,0,199,200,5,12,0,0,200,201,3,0,0,0,201,
        202,5,13,0,0,202,204,1,0,0,0,203,190,1,0,0,0,203,198,1,0,0,0,204,
        15,1,0,0,0,205,206,5,9,0,0,206,207,3,6,3,0,207,208,5,12,0,0,208,
        209,3,0,0,0,209,210,5,13,0,0,210,17,1,0,0,0,14,24,26,47,55,63,65,
        100,114,116,153,180,188,196,203
    ]

class MiniJavaParser ( Parser ):

    grammarFileName = "MiniJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print('", "'int'", "'char'", "'string'", 
                     "'float'", "'bool'", "'else if'", "'else'", "'while'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", 
                     "'.'", "'='", "'>'", "'<'", "'!'", "'?'", "'=='", "'<='", 
                     "'>='", "'!='", "'&&'", "'||'", "'++'", "'--'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'+='", "'-='", "'*='", 
                     "'/='", "'if'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "LBRACK", "RBRACK", "SEMICOLON", "COMMA", 
                      "DOT", "ASSIGN", "GT", "LT", "NOT", "QUESTION", "EQUAL", 
                      "LE", "GE", "NOTEQUAL", "AND", "OR", "INC", "DEC", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "IF", "WS", "INT", "STRING", 
                      "BOOL", "FLOAT", "CHAR", "VARIABLE" ]

    RULE_prog = 0
    RULE_assignments = 1
    RULE_arithmetics = 2
    RULE_logical = 3
    RULE_print = 4
    RULE_declaration = 5
    RULE_conditionals = 6
    RULE_conditionalsExtend = 7
    RULE_whileloop = 8

    ruleNames =  [ "prog", "assignments", "arithmetics", "logical", "print", 
                   "declaration", "conditionals", "conditionalsExtend", 
                   "whileloop" ]

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
    LPAREN=10
    RPAREN=11
    LBRACE=12
    RBRACE=13
    LBRACK=14
    RBRACK=15
    SEMICOLON=16
    COMMA=17
    DOT=18
    ASSIGN=19
    GT=20
    LT=21
    NOT=22
    QUESTION=23
    EQUAL=24
    LE=25
    GE=26
    NOTEQUAL=27
    AND=28
    OR=29
    INC=30
    DEC=31
    ADD=32
    SUB=33
    MUL=34
    DIV=35
    MOD=36
    ADD_ASSIGN=37
    SUB_ASSIGN=38
    MUL_ASSIGN=39
    DIV_ASSIGN=40
    IF=41
    WS=42
    INT=43
    STRING=44
    BOOL=45
    FLOAT=46
    CHAR=47
    VARIABLE=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetics(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ArithmeticsContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ArithmeticsContext,i)


        def print_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.PrintContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.PrintContext,i)


        def logical(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.LogicalContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.LogicalContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.DeclarationContext,i)


        def conditionals(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ConditionalsContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ConditionalsContext,i)


        def assignments(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.AssignmentsContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.AssignmentsContext,i)


        def getRuleIndex(self):
            return MiniJavaParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MiniJavaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 398023213450366) != 0:
                self.state = 24
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 18
                    self.arithmetics(0)
                    pass

                elif la_ == 2:
                    self.state = 19
                    self.print_()
                    pass

                elif la_ == 3:
                    self.state = 20
                    self.logical(0)
                    pass

                elif la_ == 4:
                    self.state = 21
                    self.declaration()
                    pass

                elif la_ == 5:
                    self.state = 22
                    self.conditionals()
                    pass

                elif la_ == 6:
                    self.state = 23
                    self.assignments()
                    pass


                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniJavaParser.RULE_assignments

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArithmeticsAssContext(AssignmentsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.AssignmentsContext
            super().__init__(parser)
            self.expr = None # ArithmeticsContext
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MiniJavaParser.VARIABLE, 0)
        def ASSIGN(self):
            return self.getToken(MiniJavaParser.ASSIGN, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)
        def arithmetics(self):
            return self.getTypedRuleContext(MiniJavaParser.ArithmeticsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticsAss" ):
                listener.enterArithmeticsAss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticsAss" ):
                listener.exitArithmeticsAss(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticsAss" ):
                return visitor.visitArithmeticsAss(self)
            else:
                return visitor.visitChildren(self)


    class StringAssContext(AssignmentsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.AssignmentsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MiniJavaParser.VARIABLE, 0)
        def ASSIGN(self):
            return self.getToken(MiniJavaParser.ASSIGN, 0)
        def STRING(self):
            return self.getToken(MiniJavaParser.STRING, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringAss" ):
                listener.enterStringAss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringAss" ):
                listener.exitStringAss(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringAss" ):
                return visitor.visitStringAss(self)
            else:
                return visitor.visitChildren(self)


    class BoolAssContext(AssignmentsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.AssignmentsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MiniJavaParser.VARIABLE, 0)
        def ASSIGN(self):
            return self.getToken(MiniJavaParser.ASSIGN, 0)
        def CHAR(self):
            return self.getToken(MiniJavaParser.CHAR, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolAss" ):
                listener.enterBoolAss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolAss" ):
                listener.exitBoolAss(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolAss" ):
                return visitor.visitBoolAss(self)
            else:
                return visitor.visitChildren(self)


    class LogicalAssContext(AssignmentsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.AssignmentsContext
            super().__init__(parser)
            self.expr = None # LogicalContext
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MiniJavaParser.VARIABLE, 0)
        def ASSIGN(self):
            return self.getToken(MiniJavaParser.ASSIGN, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)
        def logical(self):
            return self.getTypedRuleContext(MiniJavaParser.LogicalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAss" ):
                listener.enterLogicalAss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAss" ):
                listener.exitLogicalAss(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAss" ):
                return visitor.visitLogicalAss(self)
            else:
                return visitor.visitChildren(self)



    def assignments(self):

        localctx = MiniJavaParser.AssignmentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assignments)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = MiniJavaParser.LogicalAssContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(MiniJavaParser.VARIABLE)
                self.state = 30
                self.match(MiniJavaParser.ASSIGN)
                self.state = 31
                localctx.expr = self.logical(0)
                self.state = 32
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 2:
                localctx = MiniJavaParser.ArithmeticsAssContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(MiniJavaParser.VARIABLE)
                self.state = 35
                self.match(MiniJavaParser.ASSIGN)
                self.state = 36
                localctx.expr = self.arithmetics(0)
                self.state = 37
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 3:
                localctx = MiniJavaParser.StringAssContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(MiniJavaParser.VARIABLE)
                self.state = 40
                self.match(MiniJavaParser.ASSIGN)
                self.state = 41
                self.match(MiniJavaParser.STRING)
                self.state = 42
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 4:
                localctx = MiniJavaParser.BoolAssContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.match(MiniJavaParser.VARIABLE)
                self.state = 44
                self.match(MiniJavaParser.ASSIGN)
                self.state = 45
                self.match(MiniJavaParser.CHAR)
                self.state = 46
                self.match(MiniJavaParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniJavaParser.RULE_arithmetics

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AtomArithmContext(ArithmeticsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ArithmeticsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiniJavaParser.INT, 0)
        def FLOAT(self):
            return self.getToken(MiniJavaParser.FLOAT, 0)
        def VARIABLE(self):
            return self.getToken(MiniJavaParser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomArithm" ):
                listener.enterAtomArithm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomArithm" ):
                listener.exitAtomArithm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomArithm" ):
                return visitor.visitAtomArithm(self)
            else:
                return visitor.visitChildren(self)


    class ParenArithmContext(ArithmeticsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ArithmeticsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MiniJavaParser.LPAREN, 0)
        def arithmetics(self):
            return self.getTypedRuleContext(MiniJavaParser.ArithmeticsContext,0)

        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenArithm" ):
                listener.enterParenArithm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenArithm" ):
                listener.exitParenArithm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenArithm" ):
                return visitor.visitParenArithm(self)
            else:
                return visitor.visitChildren(self)


    class OpArithmContext(ArithmeticsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ArithmeticsContext
            super().__init__(parser)
            self.left = None # ArithmeticsContext
            self.op = None # Token
            self.right = None # ArithmeticsContext
            self.copyFrom(ctx)

        def arithmetics(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ArithmeticsContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ArithmeticsContext,i)

        def MUL(self):
            return self.getToken(MiniJavaParser.MUL, 0)
        def DIV(self):
            return self.getToken(MiniJavaParser.DIV, 0)
        def MOD(self):
            return self.getToken(MiniJavaParser.MOD, 0)
        def ADD(self):
            return self.getToken(MiniJavaParser.ADD, 0)
        def SUB(self):
            return self.getToken(MiniJavaParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpArithm" ):
                listener.enterOpArithm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpArithm" ):
                listener.exitOpArithm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpArithm" ):
                return visitor.visitOpArithm(self)
            else:
                return visitor.visitChildren(self)



    def arithmetics(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniJavaParser.ArithmeticsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_arithmetics, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = MiniJavaParser.ParenArithmContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 50
                self.match(MiniJavaParser.LPAREN)
                self.state = 51
                self.arithmetics(0)
                self.state = 52
                self.match(MiniJavaParser.RPAREN)
                pass
            elif token in [43, 46, 48]:
                localctx = MiniJavaParser.AtomArithmContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 360639813910528) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 63
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MiniJavaParser.OpArithmContext(self, MiniJavaParser.ArithmeticsContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetics)
                        self.state = 57
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 58
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        localctx.right = self.arithmetics(5)
                        pass

                    elif la_ == 2:
                        localctx = MiniJavaParser.OpArithmContext(self, MiniJavaParser.ArithmeticsContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetics)
                        self.state = 60
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 61
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==32 or _la==33):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 62
                        localctx.right = self.arithmetics(4)
                        pass

             
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniJavaParser.RULE_logical

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LogicalEqualsContext(LogicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.LogicalContext
            super().__init__(parser)
            self.left = None # LogicalContext
            self.op = None # Token
            self.right = None # LogicalContext
            self.copyFrom(ctx)

        def logical(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.LogicalContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.LogicalContext,i)

        def EQUAL(self):
            return self.getToken(MiniJavaParser.EQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalEquals" ):
                listener.enterLogicalEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalEquals" ):
                listener.exitLogicalEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalEquals" ):
                return visitor.visitLogicalEquals(self)
            else:
                return visitor.visitChildren(self)


    class LogicalNotContext(LogicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.LogicalContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def logical(self):
            return self.getTypedRuleContext(MiniJavaParser.LogicalContext,0)

        def NOT(self):
            return self.getToken(MiniJavaParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalNot" ):
                listener.enterLogicalNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalNot" ):
                listener.exitLogicalNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalNot" ):
                return visitor.visitLogicalNot(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticsEqualsContext(LogicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.LogicalContext
            super().__init__(parser)
            self.left = None # ArithmeticsContext
            self.op = None # Token
            self.right = None # ArithmeticsContext
            self.copyFrom(ctx)

        def arithmetics(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ArithmeticsContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ArithmeticsContext,i)

        def EQUAL(self):
            return self.getToken(MiniJavaParser.EQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticsEquals" ):
                listener.enterArithmeticsEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticsEquals" ):
                listener.exitArithmeticsEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticsEquals" ):
                return visitor.visitArithmeticsEquals(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticsBiggerContext(LogicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.LogicalContext
            super().__init__(parser)
            self.left = None # ArithmeticsContext
            self.op = None # Token
            self.right = None # ArithmeticsContext
            self.copyFrom(ctx)

        def arithmetics(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ArithmeticsContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ArithmeticsContext,i)

        def GT(self):
            return self.getToken(MiniJavaParser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticsBigger" ):
                listener.enterArithmeticsBigger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticsBigger" ):
                listener.exitArithmeticsBigger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticsBigger" ):
                return visitor.visitArithmeticsBigger(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticsSmallerEqualsContext(LogicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.LogicalContext
            super().__init__(parser)
            self.left = None # ArithmeticsContext
            self.op = None # Token
            self.right = None # ArithmeticsContext
            self.copyFrom(ctx)

        def arithmetics(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ArithmeticsContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ArithmeticsContext,i)

        def LE(self):
            return self.getToken(MiniJavaParser.LE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticsSmallerEquals" ):
                listener.enterArithmeticsSmallerEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticsSmallerEquals" ):
                listener.exitArithmeticsSmallerEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticsSmallerEquals" ):
                return visitor.visitArithmeticsSmallerEquals(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticsBiggerEqualsContext(LogicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.LogicalContext
            super().__init__(parser)
            self.left = None # ArithmeticsContext
            self.op = None # Token
            self.right = None # ArithmeticsContext
            self.copyFrom(ctx)

        def arithmetics(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ArithmeticsContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ArithmeticsContext,i)

        def GE(self):
            return self.getToken(MiniJavaParser.GE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticsBiggerEquals" ):
                listener.enterArithmeticsBiggerEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticsBiggerEquals" ):
                listener.exitArithmeticsBiggerEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticsBiggerEquals" ):
                return visitor.visitArithmeticsBiggerEquals(self)
            else:
                return visitor.visitChildren(self)


    class LogicalAndContext(LogicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.LogicalContext
            super().__init__(parser)
            self.left = None # LogicalContext
            self.op = None # Token
            self.right = None # LogicalContext
            self.copyFrom(ctx)

        def logical(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.LogicalContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.LogicalContext,i)

        def AND(self):
            return self.getToken(MiniJavaParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAnd" ):
                listener.enterLogicalAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAnd" ):
                listener.exitLogicalAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAnd" ):
                return visitor.visitLogicalAnd(self)
            else:
                return visitor.visitChildren(self)


    class LogicalParenContext(LogicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.LogicalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MiniJavaParser.LPAREN, 0)
        def logical(self):
            return self.getTypedRuleContext(MiniJavaParser.LogicalContext,0)

        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalParen" ):
                listener.enterLogicalParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalParen" ):
                listener.exitLogicalParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalParen" ):
                return visitor.visitLogicalParen(self)
            else:
                return visitor.visitChildren(self)


    class LogicalAtomContext(LogicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.LogicalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(MiniJavaParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAtom" ):
                listener.enterLogicalAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAtom" ):
                listener.exitLogicalAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAtom" ):
                return visitor.visitLogicalAtom(self)
            else:
                return visitor.visitChildren(self)


    class LogicalNotEqualsContext(LogicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.LogicalContext
            super().__init__(parser)
            self.left = None # LogicalContext
            self.op = None # Token
            self.right = None # LogicalContext
            self.copyFrom(ctx)

        def logical(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.LogicalContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.LogicalContext,i)

        def NOTEQUAL(self):
            return self.getToken(MiniJavaParser.NOTEQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalNotEquals" ):
                listener.enterLogicalNotEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalNotEquals" ):
                listener.exitLogicalNotEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalNotEquals" ):
                return visitor.visitLogicalNotEquals(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticsSmallerContext(LogicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.LogicalContext
            super().__init__(parser)
            self.left = None # ArithmeticsContext
            self.op = None # Token
            self.right = None # ArithmeticsContext
            self.copyFrom(ctx)

        def arithmetics(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ArithmeticsContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ArithmeticsContext,i)

        def LT(self):
            return self.getToken(MiniJavaParser.LT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticsSmaller" ):
                listener.enterArithmeticsSmaller(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticsSmaller" ):
                listener.exitArithmeticsSmaller(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticsSmaller" ):
                return visitor.visitArithmeticsSmaller(self)
            else:
                return visitor.visitChildren(self)


    class LogicalOrContext(LogicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.LogicalContext
            super().__init__(parser)
            self.left = None # LogicalContext
            self.op = None # Token
            self.right = None # LogicalContext
            self.copyFrom(ctx)

        def logical(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.LogicalContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.LogicalContext,i)

        def OR(self):
            return self.getToken(MiniJavaParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOr" ):
                listener.enterLogicalOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOr" ):
                listener.exitLogicalOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOr" ):
                return visitor.visitLogicalOr(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticsNotEqualsContext(LogicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.LogicalContext
            super().__init__(parser)
            self.left = None # ArithmeticsContext
            self.op = None # Token
            self.right = None # ArithmeticsContext
            self.copyFrom(ctx)

        def arithmetics(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ArithmeticsContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ArithmeticsContext,i)

        def NOTEQUAL(self):
            return self.getToken(MiniJavaParser.NOTEQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticsNotEquals" ):
                listener.enterArithmeticsNotEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticsNotEquals" ):
                listener.exitArithmeticsNotEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticsNotEquals" ):
                return visitor.visitArithmeticsNotEquals(self)
            else:
                return visitor.visitChildren(self)



    def logical(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniJavaParser.LogicalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_logical, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = MiniJavaParser.ArithmeticsEqualsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 69
                localctx.left = self.arithmetics(0)
                self.state = 70
                localctx.op = self.match(MiniJavaParser.EQUAL)
                self.state = 71
                localctx.right = self.arithmetics(0)
                pass

            elif la_ == 2:
                localctx = MiniJavaParser.ArithmeticsNotEqualsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 73
                localctx.left = self.arithmetics(0)
                self.state = 74
                localctx.op = self.match(MiniJavaParser.NOTEQUAL)
                self.state = 75
                localctx.right = self.arithmetics(0)
                pass

            elif la_ == 3:
                localctx = MiniJavaParser.ArithmeticsSmallerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 77
                localctx.left = self.arithmetics(0)
                self.state = 78
                localctx.op = self.match(MiniJavaParser.LT)
                self.state = 79
                localctx.right = self.arithmetics(0)
                pass

            elif la_ == 4:
                localctx = MiniJavaParser.ArithmeticsSmallerEqualsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                localctx.left = self.arithmetics(0)
                self.state = 82
                localctx.op = self.match(MiniJavaParser.LE)
                self.state = 83
                localctx.right = self.arithmetics(0)
                pass

            elif la_ == 5:
                localctx = MiniJavaParser.ArithmeticsBiggerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 85
                localctx.left = self.arithmetics(0)
                self.state = 86
                localctx.op = self.match(MiniJavaParser.GT)
                self.state = 87
                localctx.right = self.arithmetics(0)
                pass

            elif la_ == 6:
                localctx = MiniJavaParser.ArithmeticsBiggerEqualsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 89
                localctx.left = self.arithmetics(0)
                self.state = 90
                localctx.op = self.match(MiniJavaParser.GE)
                self.state = 91
                localctx.right = self.arithmetics(0)
                pass

            elif la_ == 7:
                localctx = MiniJavaParser.LogicalNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 93
                localctx.op = self.match(MiniJavaParser.NOT)
                self.state = 94
                self.logical(3)
                pass

            elif la_ == 8:
                localctx = MiniJavaParser.LogicalParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 95
                self.match(MiniJavaParser.LPAREN)
                self.state = 96
                self.logical(0)
                self.state = 97
                self.match(MiniJavaParser.RPAREN)
                pass

            elif la_ == 9:
                localctx = MiniJavaParser.LogicalAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 99
                self.match(MiniJavaParser.BOOL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 114
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = MiniJavaParser.LogicalAndContext(self, MiniJavaParser.LogicalContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical)
                        self.state = 102
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 103
                        localctx.op = self.match(MiniJavaParser.AND)
                        self.state = 104
                        localctx.right = self.logical(14)
                        pass

                    elif la_ == 2:
                        localctx = MiniJavaParser.LogicalOrContext(self, MiniJavaParser.LogicalContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical)
                        self.state = 105
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 106
                        localctx.op = self.match(MiniJavaParser.OR)
                        self.state = 107
                        localctx.right = self.logical(13)
                        pass

                    elif la_ == 3:
                        localctx = MiniJavaParser.LogicalEqualsContext(self, MiniJavaParser.LogicalContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical)
                        self.state = 108
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 109
                        localctx.op = self.match(MiniJavaParser.EQUAL)
                        self.state = 110
                        localctx.right = self.logical(12)
                        pass

                    elif la_ == 4:
                        localctx = MiniJavaParser.LogicalNotEqualsContext(self, MiniJavaParser.LogicalContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical)
                        self.state = 111
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 112
                        localctx.op = self.match(MiniJavaParser.NOTEQUAL)
                        self.state = 113
                        localctx.right = self.logical(11)
                        pass

             
                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniJavaParser.RULE_print

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintVariableContext(PrintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.PrintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MiniJavaParser.VARIABLE, 0)
        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintVariable" ):
                listener.enterPrintVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintVariable" ):
                listener.exitPrintVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintVariable" ):
                return visitor.visitPrintVariable(self)
            else:
                return visitor.visitChildren(self)


    class PrintLogicalContext(PrintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.PrintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logical(self):
            return self.getTypedRuleContext(MiniJavaParser.LogicalContext,0)

        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintLogical" ):
                listener.enterPrintLogical(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintLogical" ):
                listener.exitPrintLogical(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintLogical" ):
                return visitor.visitPrintLogical(self)
            else:
                return visitor.visitChildren(self)


    class PrintIntContext(PrintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.PrintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiniJavaParser.INT, 0)
        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintInt" ):
                listener.enterPrintInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintInt" ):
                listener.exitPrintInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintInt" ):
                return visitor.visitPrintInt(self)
            else:
                return visitor.visitChildren(self)


    class PrintBoolContext(PrintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.PrintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(MiniJavaParser.BOOL, 0)
        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintBool" ):
                listener.enterPrintBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintBool" ):
                listener.exitPrintBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintBool" ):
                return visitor.visitPrintBool(self)
            else:
                return visitor.visitChildren(self)


    class PrintArithmeticsContext(PrintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.PrintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmetics(self):
            return self.getTypedRuleContext(MiniJavaParser.ArithmeticsContext,0)

        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintArithmetics" ):
                listener.enterPrintArithmetics(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintArithmetics" ):
                listener.exitPrintArithmetics(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintArithmetics" ):
                return visitor.visitPrintArithmetics(self)
            else:
                return visitor.visitChildren(self)


    class PrintStringContext(PrintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.PrintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(MiniJavaParser.STRING, 0)
        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintString" ):
                listener.enterPrintString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintString" ):
                listener.exitPrintString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintString" ):
                return visitor.visitPrintString(self)
            else:
                return visitor.visitChildren(self)


    class PrintFloatContext(PrintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.PrintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(MiniJavaParser.FLOAT, 0)
        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintFloat" ):
                listener.enterPrintFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintFloat" ):
                listener.exitPrintFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintFloat" ):
                return visitor.visitPrintFloat(self)
            else:
                return visitor.visitChildren(self)


    class PrintCharContext(PrintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.PrintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(MiniJavaParser.CHAR, 0)
        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintChar" ):
                listener.enterPrintChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintChar" ):
                listener.exitPrintChar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintChar" ):
                return visitor.visitPrintChar(self)
            else:
                return visitor.visitChildren(self)



    def print_(self):

        localctx = MiniJavaParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_print)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = MiniJavaParser.PrintLogicalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(MiniJavaParser.T__0)
                self.state = 120
                self.logical(0)
                self.state = 121
                self.match(MiniJavaParser.RPAREN)
                self.state = 122
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 2:
                localctx = MiniJavaParser.PrintStringContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(MiniJavaParser.T__0)
                self.state = 125
                self.match(MiniJavaParser.STRING)
                self.state = 126
                self.match(MiniJavaParser.RPAREN)
                self.state = 127
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 3:
                localctx = MiniJavaParser.PrintIntContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.match(MiniJavaParser.T__0)
                self.state = 129
                self.match(MiniJavaParser.INT)
                self.state = 130
                self.match(MiniJavaParser.RPAREN)
                self.state = 131
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 4:
                localctx = MiniJavaParser.PrintFloatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.match(MiniJavaParser.T__0)
                self.state = 133
                self.match(MiniJavaParser.FLOAT)
                self.state = 134
                self.match(MiniJavaParser.RPAREN)
                self.state = 135
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 5:
                localctx = MiniJavaParser.PrintBoolContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 136
                self.match(MiniJavaParser.T__0)
                self.state = 137
                self.match(MiniJavaParser.BOOL)
                self.state = 138
                self.match(MiniJavaParser.RPAREN)
                self.state = 139
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 6:
                localctx = MiniJavaParser.PrintCharContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 140
                self.match(MiniJavaParser.T__0)
                self.state = 141
                self.match(MiniJavaParser.CHAR)
                self.state = 142
                self.match(MiniJavaParser.RPAREN)
                self.state = 143
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 7:
                localctx = MiniJavaParser.PrintVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 144
                self.match(MiniJavaParser.T__0)
                self.state = 145
                self.match(MiniJavaParser.VARIABLE)
                self.state = 146
                self.match(MiniJavaParser.RPAREN)
                self.state = 147
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 8:
                localctx = MiniJavaParser.PrintArithmeticsContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 148
                self.match(MiniJavaParser.T__0)
                self.state = 149
                self.arithmetics(0)
                self.state = 150
                self.match(MiniJavaParser.RPAREN)
                self.state = 151
                self.match(MiniJavaParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniJavaParser.RULE_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FloatDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MiniJavaParser.VARIABLE, 0)
        def ASSIGN(self):
            return self.getToken(MiniJavaParser.ASSIGN, 0)
        def FLOAT(self):
            return self.getToken(MiniJavaParser.FLOAT, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatDeclaration" ):
                listener.enterFloatDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatDeclaration" ):
                listener.exitFloatDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatDeclaration" ):
                return visitor.visitFloatDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class CharDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MiniJavaParser.VARIABLE, 0)
        def ASSIGN(self):
            return self.getToken(MiniJavaParser.ASSIGN, 0)
        def CHAR(self):
            return self.getToken(MiniJavaParser.CHAR, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharDeclaration" ):
                listener.enterCharDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharDeclaration" ):
                listener.exitCharDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharDeclaration" ):
                return visitor.visitCharDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class StringDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MiniJavaParser.VARIABLE, 0)
        def ASSIGN(self):
            return self.getToken(MiniJavaParser.ASSIGN, 0)
        def STRING(self):
            return self.getToken(MiniJavaParser.STRING, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringDeclaration" ):
                listener.enterStringDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringDeclaration" ):
                listener.exitStringDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringDeclaration" ):
                return visitor.visitStringDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class BoolDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MiniJavaParser.VARIABLE, 0)
        def ASSIGN(self):
            return self.getToken(MiniJavaParser.ASSIGN, 0)
        def BOOL(self):
            return self.getToken(MiniJavaParser.BOOL, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolDeclaration" ):
                listener.enterBoolDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolDeclaration" ):
                listener.exitBoolDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolDeclaration" ):
                return visitor.visitBoolDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class IntDeclarationContext(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MiniJavaParser.VARIABLE, 0)
        def ASSIGN(self):
            return self.getToken(MiniJavaParser.ASSIGN, 0)
        def INT(self):
            return self.getToken(MiniJavaParser.INT, 0)
        def SEMICOLON(self):
            return self.getToken(MiniJavaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntDeclaration" ):
                listener.enterIntDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntDeclaration" ):
                listener.exitIntDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntDeclaration" ):
                return visitor.visitIntDeclaration(self)
            else:
                return visitor.visitChildren(self)



    def declaration(self):

        localctx = MiniJavaParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaration)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = MiniJavaParser.IntDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(MiniJavaParser.T__1)
                self.state = 156
                self.match(MiniJavaParser.VARIABLE)
                self.state = 157
                self.match(MiniJavaParser.ASSIGN)
                self.state = 158
                self.match(MiniJavaParser.INT)
                self.state = 159
                self.match(MiniJavaParser.SEMICOLON)
                pass
            elif token in [3]:
                localctx = MiniJavaParser.CharDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(MiniJavaParser.T__2)
                self.state = 161
                self.match(MiniJavaParser.VARIABLE)
                self.state = 162
                self.match(MiniJavaParser.ASSIGN)
                self.state = 163
                self.match(MiniJavaParser.CHAR)
                self.state = 164
                self.match(MiniJavaParser.SEMICOLON)
                pass
            elif token in [4]:
                localctx = MiniJavaParser.StringDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.match(MiniJavaParser.T__3)
                self.state = 166
                self.match(MiniJavaParser.VARIABLE)
                self.state = 167
                self.match(MiniJavaParser.ASSIGN)
                self.state = 168
                self.match(MiniJavaParser.STRING)
                self.state = 169
                self.match(MiniJavaParser.SEMICOLON)
                pass
            elif token in [5]:
                localctx = MiniJavaParser.FloatDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 170
                self.match(MiniJavaParser.T__4)
                self.state = 171
                self.match(MiniJavaParser.VARIABLE)
                self.state = 172
                self.match(MiniJavaParser.ASSIGN)
                self.state = 173
                self.match(MiniJavaParser.FLOAT)
                self.state = 174
                self.match(MiniJavaParser.SEMICOLON)
                pass
            elif token in [6]:
                localctx = MiniJavaParser.BoolDeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 175
                self.match(MiniJavaParser.T__5)
                self.state = 176
                self.match(MiniJavaParser.VARIABLE)
                self.state = 177
                self.match(MiniJavaParser.ASSIGN)
                self.state = 178
                self.match(MiniJavaParser.BOOL)
                self.state = 179
                self.match(MiniJavaParser.SEMICOLON)
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


    class ConditionalsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniJavaParser.RULE_conditionals

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StartIfContext(ConditionalsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ConditionalsContext
            super().__init__(parser)
            self.cond = None # LogicalContext
            self.body = None # ProgContext
            self.moreConditions = None # ConditionalsExtendContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MiniJavaParser.IF, 0)
        def LBRACE(self):
            return self.getToken(MiniJavaParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(MiniJavaParser.RBRACE, 0)
        def logical(self):
            return self.getTypedRuleContext(MiniJavaParser.LogicalContext,0)

        def prog(self):
            return self.getTypedRuleContext(MiniJavaParser.ProgContext,0)

        def conditionalsExtend(self):
            return self.getTypedRuleContext(MiniJavaParser.ConditionalsExtendContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartIf" ):
                listener.enterStartIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartIf" ):
                listener.exitStartIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStartIf" ):
                return visitor.visitStartIf(self)
            else:
                return visitor.visitChildren(self)



    def conditionals(self):

        localctx = MiniJavaParser.ConditionalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_conditionals)
        self._la = 0 # Token type
        try:
            localctx = MiniJavaParser.StartIfContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(MiniJavaParser.IF)
            self.state = 183
            localctx.cond = self.logical(0)
            self.state = 184
            self.match(MiniJavaParser.LBRACE)
            self.state = 185
            localctx.body = self.prog()
            self.state = 186
            self.match(MiniJavaParser.RBRACE)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==8:
                self.state = 187
                localctx.moreConditions = self.conditionalsExtend()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalsExtendContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniJavaParser.RULE_conditionalsExtend

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ElseContext(ConditionalsExtendContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ConditionalsExtendContext
            super().__init__(parser)
            self.body = None # ProgContext
            self.copyFrom(ctx)

        def LBRACE(self):
            return self.getToken(MiniJavaParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(MiniJavaParser.RBRACE, 0)
        def prog(self):
            return self.getTypedRuleContext(MiniJavaParser.ProgContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse" ):
                return visitor.visitElse(self)
            else:
                return visitor.visitChildren(self)


    class ElifContext(ConditionalsExtendContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ConditionalsExtendContext
            super().__init__(parser)
            self.cond = None # LogicalContext
            self.body = None # ProgContext
            self.moreConditions = None # ConditionalsExtendContext
            self.copyFrom(ctx)

        def LBRACE(self):
            return self.getToken(MiniJavaParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(MiniJavaParser.RBRACE, 0)
        def logical(self):
            return self.getTypedRuleContext(MiniJavaParser.LogicalContext,0)

        def prog(self):
            return self.getTypedRuleContext(MiniJavaParser.ProgContext,0)

        def conditionalsExtend(self):
            return self.getTypedRuleContext(MiniJavaParser.ConditionalsExtendContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif" ):
                listener.enterElif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif" ):
                listener.exitElif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif" ):
                return visitor.visitElif(self)
            else:
                return visitor.visitChildren(self)



    def conditionalsExtend(self):

        localctx = MiniJavaParser.ConditionalsExtendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_conditionalsExtend)
        self._la = 0 # Token type
        try:
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = MiniJavaParser.ElifContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(MiniJavaParser.T__6)
                self.state = 191
                localctx.cond = self.logical(0)
                self.state = 192
                self.match(MiniJavaParser.LBRACE)
                self.state = 193
                localctx.body = self.prog()
                self.state = 194
                self.match(MiniJavaParser.RBRACE)
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7 or _la==8:
                    self.state = 195
                    localctx.moreConditions = self.conditionalsExtend()


                pass
            elif token in [8]:
                localctx = MiniJavaParser.ElseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.match(MiniJavaParser.T__7)
                self.state = 199
                self.match(MiniJavaParser.LBRACE)
                self.state = 200
                localctx.body = self.prog()
                self.state = 201
                self.match(MiniJavaParser.RBRACE)
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


    class WhileloopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cond = None # LogicalContext

        def LBRACE(self):
            return self.getToken(MiniJavaParser.LBRACE, 0)

        def prog(self):
            return self.getTypedRuleContext(MiniJavaParser.ProgContext,0)


        def RBRACE(self):
            return self.getToken(MiniJavaParser.RBRACE, 0)

        def logical(self):
            return self.getTypedRuleContext(MiniJavaParser.LogicalContext,0)


        def getRuleIndex(self):
            return MiniJavaParser.RULE_whileloop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileloop" ):
                listener.enterWhileloop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileloop" ):
                listener.exitWhileloop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileloop" ):
                return visitor.visitWhileloop(self)
            else:
                return visitor.visitChildren(self)




    def whileloop(self):

        localctx = MiniJavaParser.WhileloopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(MiniJavaParser.T__8)
            self.state = 206
            localctx.cond = self.logical(0)
            self.state = 207
            self.match(MiniJavaParser.LBRACE)
            self.state = 208
            self.prog()
            self.state = 209
            self.match(MiniJavaParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.arithmetics_sempred
        self._predicates[3] = self.logical_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmetics_sempred(self, localctx:ArithmeticsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def logical_sempred(self, localctx:LogicalContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         




