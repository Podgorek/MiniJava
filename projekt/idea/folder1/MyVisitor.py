from antlr4 import ParseTreeVisitor
from MiniJavaVisitor import MiniJavaVisitor
from MiniJavaParser import MiniJavaParser
from MyListener import MyListener

class MyVisitor(MiniJavaVisitor):

    def __init__(self, variables):
        self.variables = variables


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
        if ctx.getText() in self.variables["bool"]:
            return self.variables["bool"][ctx.getText()]
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
        if ctx.getText() in self.variables and ("int"==self.variables[ctx.getText()][0] or "float"==self.variables[ctx.getText()][0]):
            return self.variables[ctx.getText()][1]
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
        print(float(ctx.getText()))


    # Visit a parse tree produced by MiniJavaParser#printArithmetics.
    def visitPrintArithmetics(self, ctx:MiniJavaParser.PrintArithmeticsContext):
        print(self.visit(ctx.arithmetics()))


    # Visit a parse tree produced by MiniJavaParser#printBool.
    def visitPrintLogical(self, ctx:MiniJavaParser.PrintBoolContext):
        print(self.visit(ctx.logical()))


    # Visit a parse tree produced by MiniJavaParser#printChar.
    def visitPrintChar(self, ctx:MiniJavaParser.PrintCharContext):
        print(ctx.CHAR())

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


    def visitConditionals(self, ctx:MiniJavaParser.ConditionalsContext):
        print(ctx.getText())

    def visitArithmeticsEquals(self, ctx:MiniJavaParser.ArithmeticsEqualsContext):
        return self.visit(ctx.right)==self.visit(ctx.left)

    def visitArithmeticsBigger(self, ctx:MiniJavaParser.ArithmeticsBiggerContext):
        return self.visit(ctx.left) > self.visit(ctx.right)

    def visitArithmeticsBiggerEquals(self, ctx:MiniJavaParser.ArithmeticsBiggerEqualsContext):
        return self.visit(ctx.left) >= self.visit(ctx.right)

    def visitArithmeticsSmaller(self, ctx:MiniJavaParser.ArithmeticsSmallerContext):
        return self.visit(ctx.left) < self.visit(ctx.right)

    def visitArithmeticsSmallerEquals(self, ctx:MiniJavaParser.ArithmeticsSmallerEqualsContext):
        return self.visit(ctx.left) <= self.visit(ctx.right)

    def visitLogicalEquals(self, ctx:MiniJavaParser.LogicalEqualsContext):
        return self.visit(ctx.left) == self.visit(ctx.right)

    def visitArithmeticsNotEquals(self, ctx:MiniJavaParser.ArithmeticsNotEqualsContext):
        return self.visit(ctx.left) != self.visit(ctx.right)

    def visitStartIf(self, ctx:MiniJavaParser.StartIfContext):
        if self.visit(ctx.cond):
            self.visit(ctx.body)
        else:
            try:
                self.visit(ctx.moreConditions)
            except AttributeError:
                pass

    # Visit a parse tree produced by MiniJavaParser#elif.
    def visitElif(self, ctx:MiniJavaParser.ElifContext):
        if self.visit(ctx.cond):
            self.visit(ctx.body)
        else:
            try:
                self.visit(ctx.moreConditions)
            except AttributeError:
                pass

    # Visit a parse tree produced by MiniJavaParser#else.
    def visitElse(self, ctx:MiniJavaParser.ElseContext):
        self.visit(ctx.body)

    def visitPrintVariable(self, ctx:MiniJavaParser.PrintVariableContext):
        if ctx.getText()[6:-2] in self.variables:
            print(self.variables[ctx.getText()[6:-2]][1])

    def visitLogicalAss(self, ctx:MiniJavaParser.LogicalAssContext):
        var = self.visit(ctx.expr)
        name = ctx.getText().split("=")[0]
        if name in self.variables:
            self.variables[name][1] = var

    def visitArithmeticsAss(self, ctx: MiniJavaParser.ArithmeticsAssContext):
        var = self.visit(ctx.expr)
        name = ctx.getText().split("=")[0]
        if name in self.variables:
            self.variables[name][1] = var
        print(self.variables)