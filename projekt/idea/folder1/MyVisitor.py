from antlr4 import ParseTreeVisitor
from MiniJavaVisitor import MiniJavaVisitor
from MiniJavaParser import MiniJavaParser


class MyVisitor(MiniJavaVisitor):
    def visitProg(self, ctx:MiniJavaParser.ProgContext):
        return self.visitChildren(ctx)

    def visitLogicalNot(self, ctx:MiniJavaParser.LogicalNotContext):
        return not self.visit(ctx.logical())


    # Visit a parse tree produced by MiniJavaParser#logicalAnd.
    def visitLogicalAnd(self, ctx:MiniJavaParser.LogicalAndContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left and right


    # Visit a parse tree produced by MiniJavaParser#logicalParen.
    def visitLogicalParen(self, ctx:MiniJavaParser.LogicalParenContext):
        return self.visit(ctx.logical())

    # Visit a parse tree produced by MiniJavaParser#logicalOr.
    def visitLogicalOr(self, ctx:MiniJavaParser.LogicalOrContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return left or right


    # Visit a parse tree produced by MiniJavaParser#logicalAtom.
    def visitLogicalAtom(self, ctx:MiniJavaParser.LogicalAtomContext):
        return True if ctx.getText()=="true" else False

    # Visit a parse tree produced by MiniJavaParser#opExpr.
    def visitOpArithm(self, ctx):

        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text

        opchar1 = op[0]
        if opchar1 == '*':
            val = left * right
        elif opchar1 == '/':
            val = left / right
        elif opchar1 == '+':
            val = left + right
        elif opchar1 == '-':
            val = left - right
        elif opchar1 == '%':
            val = left % right
        else:
            raise ValueError("Unknown operator " + op)
        return val

    def visitAtomArithm(self, ctx):
        try:
            return int(ctx.getText())
        except ValueError:
            return float(ctx.getText())


    def visitParenArithm(self, ctx):
        return self.visit(ctx.arithmetics())


    # Visit a parse tree produced by MiniJavaParser#printString.
    def visitPrintString(self, ctx:MiniJavaParser.PrintStringContext):
        print(ctx.STRING())


    # Visit a parse tree produced by MiniJavaParser#printInt.
    def visitPrintInt(self, ctx:MiniJavaParser.PrintIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#printFloat.
    def visitPrintFloat(self, ctx:MiniJavaParser.PrintFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#printArithmetics.
    def visitPrintArithmetics(self, ctx:MiniJavaParser.PrintArithmeticsContext):
        print(self.visit(ctx.arithmetics()))


    # Visit a parse tree produced by MiniJavaParser#printBool.
    def visitPrintLogical(self, ctx:MiniJavaParser.PrintBoolContext):
        print(self.visit(ctx.logical()))


    # Visit a parse tree produced by MiniJavaParser#printChar.
    def visitPrintChar(self, ctx:MiniJavaParser.PrintCharContext):
        return self.visitChildren(ctx)