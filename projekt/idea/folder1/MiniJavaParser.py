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
        4,1,39,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,23,8,1,1,1,1,1,1,1,
        1,1,1,1,1,1,5,1,31,8,1,10,1,12,1,34,9,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,3,2,44,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,52,8,2,10,2,12,2,
        55,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,
        3,87,8,3,1,3,0,2,2,4,4,0,2,4,6,0,3,2,0,34,34,37,37,1,0,26,28,1,0,
        24,25,100,0,13,1,0,0,0,2,22,1,0,0,0,4,43,1,0,0,0,6,86,1,0,0,0,8,
        12,3,2,1,0,9,12,3,6,3,0,10,12,3,4,2,0,11,8,1,0,0,0,11,9,1,0,0,0,
        11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,
        0,0,15,13,1,0,0,0,16,17,6,1,-1,0,17,18,5,2,0,0,18,19,3,2,1,0,19,
        20,5,3,0,0,20,23,1,0,0,0,21,23,7,0,0,0,22,16,1,0,0,0,22,21,1,0,0,
        0,23,32,1,0,0,0,24,25,10,4,0,0,25,26,7,1,0,0,26,31,3,2,1,5,27,28,
        10,3,0,0,28,29,7,2,0,0,29,31,3,2,1,4,30,24,1,0,0,0,30,27,1,0,0,0,
        31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,3,1,0,0,0,34,32,1,0,
        0,0,35,36,6,2,-1,0,36,37,5,14,0,0,37,44,3,4,2,3,38,39,5,2,0,0,39,
        40,3,4,2,0,40,41,5,3,0,0,41,44,1,0,0,0,42,44,5,36,0,0,43,35,1,0,
        0,0,43,38,1,0,0,0,43,42,1,0,0,0,44,53,1,0,0,0,45,46,10,5,0,0,46,
        47,5,20,0,0,47,52,3,4,2,6,48,49,10,4,0,0,49,50,5,21,0,0,50,52,3,
        4,2,5,51,45,1,0,0,0,51,48,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,
        54,1,0,0,0,54,5,1,0,0,0,55,53,1,0,0,0,56,57,5,1,0,0,57,58,3,2,1,
        0,58,59,5,3,0,0,59,60,5,8,0,0,60,87,1,0,0,0,61,62,5,1,0,0,62,63,
        3,4,2,0,63,64,5,3,0,0,64,65,5,8,0,0,65,87,1,0,0,0,66,67,5,1,0,0,
        67,68,5,35,0,0,68,69,5,3,0,0,69,87,5,8,0,0,70,71,5,1,0,0,71,72,5,
        34,0,0,72,73,5,3,0,0,73,87,5,8,0,0,74,75,5,1,0,0,75,76,5,37,0,0,
        76,77,5,3,0,0,77,87,5,8,0,0,78,79,5,1,0,0,79,80,5,36,0,0,80,81,5,
        3,0,0,81,87,5,8,0,0,82,83,5,1,0,0,83,84,5,38,0,0,84,85,5,3,0,0,85,
        87,5,8,0,0,86,56,1,0,0,0,86,61,1,0,0,0,86,66,1,0,0,0,86,70,1,0,0,
        0,86,74,1,0,0,0,86,78,1,0,0,0,86,82,1,0,0,0,87,7,1,0,0,0,9,11,13,
        22,30,32,43,51,53,86
    ]

class MiniJavaParser ( Parser ):

    grammarFileName = "MiniJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print('", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "';'", "','", "'.'", "'='", "'>'", "'<'", 
                     "'!'", "'?'", "'=='", "'<='", "'>='", "'!='", "'&&'", 
                     "'||'", "'++'", "'--'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'+='", "'-='", "'*='", "'/='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "LBRACK", "RBRACK", "SEMICOLON", "COMMA", 
                      "DOT", "ASSIGN", "GT", "LT", "NOT", "QUESTION", "EQUAL", 
                      "LE", "GE", "NOTEQUAL", "AND", "OR", "INC", "DEC", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "WS", "INT", "STRING", 
                      "BOOL", "FLOAT", "CHAR", "VARIABLE" ]

    RULE_prog = 0
    RULE_arithmetics = 1
    RULE_logical = 2
    RULE_print = 3

    ruleNames =  [ "prog", "arithmetics", "logical", "print" ]

    EOF = Token.EOF
    T__0=1
    LPAREN=2
    RPAREN=3
    LBRACE=4
    RBRACE=5
    LBRACK=6
    RBRACK=7
    SEMICOLON=8
    COMMA=9
    DOT=10
    ASSIGN=11
    GT=12
    LT=13
    NOT=14
    QUESTION=15
    EQUAL=16
    LE=17
    GE=18
    NOTEQUAL=19
    AND=20
    OR=21
    INC=22
    DEC=23
    ADD=24
    SUB=25
    MUL=26
    DIV=27
    MOD=28
    ADD_ASSIGN=29
    SUB_ASSIGN=30
    MUL_ASSIGN=31
    DIV_ASSIGN=32
    WS=33
    INT=34
    STRING=35
    BOOL=36
    FLOAT=37
    CHAR=38
    VARIABLE=39

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
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 223338315782) != 0:
                self.state = 11
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 8
                    self.arithmetics(0)
                    pass

                elif la_ == 2:
                    self.state = 9
                    self.print_()
                    pass

                elif la_ == 3:
                    self.state = 10
                    self.logical(0)
                    pass


                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_arithmetics, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = MiniJavaParser.ParenArithmContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 17
                self.match(MiniJavaParser.LPAREN)
                self.state = 18
                self.arithmetics(0)
                self.state = 19
                self.match(MiniJavaParser.RPAREN)
                pass
            elif token in [34, 37]:
                localctx = MiniJavaParser.AtomArithmContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                _la = self._input.LA(1)
                if not(_la==34 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 30
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = MiniJavaParser.OpArithmContext(self, MiniJavaParser.ArithmeticsContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetics)
                        self.state = 24
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 25
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 26
                        localctx.right = self.arithmetics(5)
                        pass

                    elif la_ == 2:
                        localctx = MiniJavaParser.OpArithmContext(self, MiniJavaParser.ArithmeticsContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetics)
                        self.state = 27
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 28
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 29
                        localctx.right = self.arithmetics(4)
                        pass

             
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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



    def logical(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniJavaParser.LogicalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_logical, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                localctx = MiniJavaParser.LogicalNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 36
                localctx.op = self.match(MiniJavaParser.NOT)
                self.state = 37
                self.logical(3)
                pass
            elif token in [2]:
                localctx = MiniJavaParser.LogicalParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(MiniJavaParser.LPAREN)
                self.state = 39
                self.logical(0)
                self.state = 40
                self.match(MiniJavaParser.RPAREN)
                pass
            elif token in [36]:
                localctx = MiniJavaParser.LogicalAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(MiniJavaParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MiniJavaParser.LogicalAndContext(self, MiniJavaParser.LogicalContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical)
                        self.state = 45
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 46
                        localctx.op = self.match(MiniJavaParser.AND)
                        self.state = 47
                        localctx.right = self.logical(6)
                        pass

                    elif la_ == 2:
                        localctx = MiniJavaParser.LogicalOrContext(self, MiniJavaParser.LogicalContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical)
                        self.state = 48
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 49
                        localctx.op = self.match(MiniJavaParser.OR)
                        self.state = 50
                        localctx.right = self.logical(5)
                        pass

             
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_print)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = MiniJavaParser.PrintArithmeticsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(MiniJavaParser.T__0)
                self.state = 57
                self.arithmetics(0)
                self.state = 58
                self.match(MiniJavaParser.RPAREN)
                self.state = 59
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 2:
                localctx = MiniJavaParser.PrintLogicalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(MiniJavaParser.T__0)
                self.state = 62
                self.logical(0)
                self.state = 63
                self.match(MiniJavaParser.RPAREN)
                self.state = 64
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 3:
                localctx = MiniJavaParser.PrintStringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.match(MiniJavaParser.T__0)
                self.state = 67
                self.match(MiniJavaParser.STRING)
                self.state = 68
                self.match(MiniJavaParser.RPAREN)
                self.state = 69
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 4:
                localctx = MiniJavaParser.PrintIntContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 70
                self.match(MiniJavaParser.T__0)
                self.state = 71
                self.match(MiniJavaParser.INT)
                self.state = 72
                self.match(MiniJavaParser.RPAREN)
                self.state = 73
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 5:
                localctx = MiniJavaParser.PrintFloatContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 74
                self.match(MiniJavaParser.T__0)
                self.state = 75
                self.match(MiniJavaParser.FLOAT)
                self.state = 76
                self.match(MiniJavaParser.RPAREN)
                self.state = 77
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 6:
                localctx = MiniJavaParser.PrintBoolContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                self.match(MiniJavaParser.T__0)
                self.state = 79
                self.match(MiniJavaParser.BOOL)
                self.state = 80
                self.match(MiniJavaParser.RPAREN)
                self.state = 81
                self.match(MiniJavaParser.SEMICOLON)
                pass

            elif la_ == 7:
                localctx = MiniJavaParser.PrintCharContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 82
                self.match(MiniJavaParser.T__0)
                self.state = 83
                self.match(MiniJavaParser.CHAR)
                self.state = 84
                self.match(MiniJavaParser.RPAREN)
                self.state = 85
                self.match(MiniJavaParser.SEMICOLON)
                pass


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
        self._predicates[1] = self.arithmetics_sempred
        self._predicates[2] = self.logical_sempred
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
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




