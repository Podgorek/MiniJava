# Generated from C:/Users/admin/PycharmProjects/MiniJava/projekt/idea/MiniJava.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete generic visitor for a parse tree produced by MiniJavaParser.

class MiniJavaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniJavaParser#prog.
    def visitProg(self, ctx:MiniJavaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#intDeclaration.
    def visitIntDeclaration(self, ctx:MiniJavaParser.IntDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#charDeclaration.
    def visitCharDeclaration(self, ctx:MiniJavaParser.CharDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#stringDeclaration.
    def visitStringDeclaration(self, ctx:MiniJavaParser.StringDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#floatDeclaration.
    def visitFloatDeclaration(self, ctx:MiniJavaParser.FloatDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#boolDeclaration.
    def visitBoolDeclaration(self, ctx:MiniJavaParser.BoolDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#tempDeclaration.
    def visitTempDeclaration(self, ctx:MiniJavaParser.TempDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#arithmeticsAssFor.
    def visitArithmeticsAssFor(self, ctx:MiniJavaParser.ArithmeticsAssForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#logicalAss.
    def visitLogicalAss(self, ctx:MiniJavaParser.LogicalAssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#stringAss.
    def visitStringAss(self, ctx:MiniJavaParser.StringAssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#charAss.
    def visitCharAss(self, ctx:MiniJavaParser.CharAssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#arithmeticsAss.
    def visitArithmeticsAss(self, ctx:MiniJavaParser.ArithmeticsAssContext):
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


    # Visit a parse tree produced by MiniJavaParser#logicalEquals.
    def visitLogicalEquals(self, ctx:MiniJavaParser.LogicalEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#logicalNot.
    def visitLogicalNot(self, ctx:MiniJavaParser.LogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#arithmeticsEquals.
    def visitArithmeticsEquals(self, ctx:MiniJavaParser.ArithmeticsEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#arithmeticsBigger.
    def visitArithmeticsBigger(self, ctx:MiniJavaParser.ArithmeticsBiggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#arithmeticsSmallerEquals.
    def visitArithmeticsSmallerEquals(self, ctx:MiniJavaParser.ArithmeticsSmallerEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#arithmeticsBiggerEquals.
    def visitArithmeticsBiggerEquals(self, ctx:MiniJavaParser.ArithmeticsBiggerEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#logicalAnd.
    def visitLogicalAnd(self, ctx:MiniJavaParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#logicalParen.
    def visitLogicalParen(self, ctx:MiniJavaParser.LogicalParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#logicalAtom.
    def visitLogicalAtom(self, ctx:MiniJavaParser.LogicalAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#logicalNotEquals.
    def visitLogicalNotEquals(self, ctx:MiniJavaParser.LogicalNotEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#arithmeticsSmaller.
    def visitArithmeticsSmaller(self, ctx:MiniJavaParser.ArithmeticsSmallerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#logicalOr.
    def visitLogicalOr(self, ctx:MiniJavaParser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#arithmeticsNotEquals.
    def visitArithmeticsNotEquals(self, ctx:MiniJavaParser.ArithmeticsNotEqualsContext):
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


    # Visit a parse tree produced by MiniJavaParser#printVariable.
    def visitPrintVariable(self, ctx:MiniJavaParser.PrintVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#printArithmetics.
    def visitPrintArithmetics(self, ctx:MiniJavaParser.PrintArithmeticsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#startIf.
    def visitStartIf(self, ctx:MiniJavaParser.StartIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#elif.
    def visitElif(self, ctx:MiniJavaParser.ElifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#else.
    def visitElse(self, ctx:MiniJavaParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#whileloop.
    def visitWhileloop(self, ctx:MiniJavaParser.WhileloopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#forloop.
    def visitForloop(self, ctx:MiniJavaParser.ForloopContext):
        return self.visitChildren(ctx)



del MiniJavaParser