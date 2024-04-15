# Generated from MiniJava.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete generic visitor for a parse tree produced by MiniJavaParser.

class MiniJavaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniJavaParser#prog.
    def visitProg(self, ctx:MiniJavaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#atomArithm.
    def visitAtomArithm(self, ctx:MiniJavaParser.AtomArithmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#parenArithm.
    def visitParenArithm(self, ctx:MiniJavaParser.ParenArithmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#opArithm.
    def visitOpArithm(self, ctx:MiniJavaParser.OpArithmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#logicalNot.
    def visitLogicalNot(self, ctx:MiniJavaParser.LogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#logicalAnd.
    def visitLogicalAnd(self, ctx:MiniJavaParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#logicalParen.
    def visitLogicalParen(self, ctx:MiniJavaParser.LogicalParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#logicalOr.
    def visitLogicalOr(self, ctx:MiniJavaParser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#logicalAtom.
    def visitLogicalAtom(self, ctx:MiniJavaParser.LogicalAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#printArithmetics.
    def visitPrintArithmetics(self, ctx:MiniJavaParser.PrintArithmeticsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#printLogical.
    def visitPrintLogical(self, ctx:MiniJavaParser.PrintLogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#printString.
    def visitPrintString(self, ctx:MiniJavaParser.PrintStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#printInt.
    def visitPrintInt(self, ctx:MiniJavaParser.PrintIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#printFloat.
    def visitPrintFloat(self, ctx:MiniJavaParser.PrintFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#printBool.
    def visitPrintBool(self, ctx:MiniJavaParser.PrintBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#printChar.
    def visitPrintChar(self, ctx:MiniJavaParser.PrintCharContext):
        return self.visitChildren(ctx)



del MiniJavaParser