# Generated from MiniJava.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete listener for a parse tree produced by MiniJavaParser.
class MiniJavaListener(ParseTreeListener):

    # Enter a parse tree produced by MiniJavaParser#prog.
    def enterProg(self, ctx:MiniJavaParser.ProgContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#prog.
    def exitProg(self, ctx:MiniJavaParser.ProgContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#atomArithm.
    def enterAtomArithm(self, ctx:MiniJavaParser.AtomArithmContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#atomArithm.
    def exitAtomArithm(self, ctx:MiniJavaParser.AtomArithmContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#parenArithm.
    def enterParenArithm(self, ctx:MiniJavaParser.ParenArithmContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#parenArithm.
    def exitParenArithm(self, ctx:MiniJavaParser.ParenArithmContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#opArithm.
    def enterOpArithm(self, ctx:MiniJavaParser.OpArithmContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#opArithm.
    def exitOpArithm(self, ctx:MiniJavaParser.OpArithmContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#logicalNot.
    def enterLogicalNot(self, ctx:MiniJavaParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#logicalNot.
    def exitLogicalNot(self, ctx:MiniJavaParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#logicalAnd.
    def enterLogicalAnd(self, ctx:MiniJavaParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#logicalAnd.
    def exitLogicalAnd(self, ctx:MiniJavaParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#logicalParen.
    def enterLogicalParen(self, ctx:MiniJavaParser.LogicalParenContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#logicalParen.
    def exitLogicalParen(self, ctx:MiniJavaParser.LogicalParenContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#logicalOr.
    def enterLogicalOr(self, ctx:MiniJavaParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#logicalOr.
    def exitLogicalOr(self, ctx:MiniJavaParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#logicalAtom.
    def enterLogicalAtom(self, ctx:MiniJavaParser.LogicalAtomContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#logicalAtom.
    def exitLogicalAtom(self, ctx:MiniJavaParser.LogicalAtomContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#printArithmetics.
    def enterPrintArithmetics(self, ctx:MiniJavaParser.PrintArithmeticsContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#printArithmetics.
    def exitPrintArithmetics(self, ctx:MiniJavaParser.PrintArithmeticsContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#printLogical.
    def enterPrintLogical(self, ctx:MiniJavaParser.PrintLogicalContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#printLogical.
    def exitPrintLogical(self, ctx:MiniJavaParser.PrintLogicalContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#printString.
    def enterPrintString(self, ctx:MiniJavaParser.PrintStringContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#printString.
    def exitPrintString(self, ctx:MiniJavaParser.PrintStringContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#printInt.
    def enterPrintInt(self, ctx:MiniJavaParser.PrintIntContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#printInt.
    def exitPrintInt(self, ctx:MiniJavaParser.PrintIntContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#printFloat.
    def enterPrintFloat(self, ctx:MiniJavaParser.PrintFloatContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#printFloat.
    def exitPrintFloat(self, ctx:MiniJavaParser.PrintFloatContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#printBool.
    def enterPrintBool(self, ctx:MiniJavaParser.PrintBoolContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#printBool.
    def exitPrintBool(self, ctx:MiniJavaParser.PrintBoolContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#printChar.
    def enterPrintChar(self, ctx:MiniJavaParser.PrintCharContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#printChar.
    def exitPrintChar(self, ctx:MiniJavaParser.PrintCharContext):
        pass



del MiniJavaParser