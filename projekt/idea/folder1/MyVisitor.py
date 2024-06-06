from antlr4 import ParseTreeVisitor
from MiniJavaVisitor import MiniJavaVisitor
from MiniJavaParser import MiniJavaParser
from MyListener import MyListener

class MyVisitor(MiniJavaVisitor):

    def __init__(self, functions):
        self.variables = {}
        self.tempVariables = {}
        self.functions = functions

#region useless nie patrzec
    def visitProg(self, ctx:MiniJavaParser.ProgContext):
        return self.visitChildren(ctx)

#endregion

#region logical
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


    #Visit a parse tree produced by MiniJavaParser#logicalAtom.
    def visitLogicalAtom(self, ctx:MiniJavaParser.LogicalAtomContext):
        var = ctx.getText()
        if var in self.variables:
            return self.variables[var][1]
        return True if ctx.getText() == "true" else False

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
#endregion

#region arithmetics
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

#endregion

# region printy
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

    def visitPrintVariable(self, ctx:MiniJavaParser.PrintVariableContext):
        if ctx.getText()[6:-2] in self.variables:
            print(self.variables[ctx.getText()[6:-2]][1])
        else:
            raise Exception("Variable not declared")

# endregion

# region Deklaracje

    # Visit a parse tree produced by MiniJavaParser#charDeclaration.
    def visitCharDeclaration(self, ctx:MiniJavaParser.CharDeclarationContext):
        temp = ctx.getText().split("char")[1].split("=")
        if temp[0] in self.variables:
            raise Exception("Double declaration")
        self.variables[temp[0]] = ["char", temp[1][:-1]]

    def visitStringDeclaration(self, ctx:MiniJavaParser.StringDeclarationContext):
        temp = ctx.getText().split("\"")
        if temp[0][6:-1] in self.variables:
            raise Exception("Double declaration")
        self.variables[temp[0][6:-1]] = ["string", temp[1]]

    def visitArithmeticsIntDeclaration(self, ctx:MiniJavaParser.ArithmeticsIntDeclarationContext):
        val = int(self.visit(ctx.expr))
        name = ctx.getText().split("int")[1].split("=")[0]
        if name not in self.variables:
            self.variables[name] = ["int", val]
        else:
            raise Exception("Double declaration")

    def visitArithmeticsFloatDeclaration(self, ctx:MiniJavaParser.ArithmeticsFloatDeclarationContext):
        val = float(self.visit(ctx.expr))
        name = ctx.getText().split("float")[1].split("=")[0]
        if name not in self.variables:
            self.variables[name] = ["float", val]
        else:
            raise Exception("Double declaration")

    def visitLogicalDeclaration(self, ctx:MiniJavaParser.LogicalDeclarationContext):
        val = self.visit(ctx.expr)
        name = ctx.getText().split("bool")[1].split("=")[0]
        if name not in self.variables:
            self.variables[name] = ["bool", val]
        else:
            raise Exception("Double declaration")
# endregion

# region warunkowe
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
# endregion

#region assignments
    def visitLogicalAss(self, ctx:MiniJavaParser.LogicalAssContext):
        var = self.visit(ctx.expr)
        name = ctx.getText().split("=")[0]
        if name in self.variables:
            self.variables[name][1] = var
        else:
            raise Exception("You must declare the variable first")

    def visitArithmeticsAss(self, ctx: MiniJavaParser.ArithmeticsAssContext):
        var = self.visit(ctx.expr)
        name = ctx.getText().split("=")[0]
        if name in self.variables:
            self.variables[name][1] = var
        else:
            raise Exception("You must declare the variable first")

    def visitArithmeticsAssFor(self, ctx: MiniJavaParser.ArithmeticsAssContext):
        var = self.visit(ctx.expr)
        name = ctx.getText().split("=")[0]
        if name in self.variables:
            self.variables[name][1] = var
        else:
            raise Exception("You must declare the variable first")

    def visitStringAss(self, ctx:MiniJavaParser.StringAssContext):
        i = 0
        name = ""
        while ctx.getText()[i] != '=':
            name += ctx.getText()[i]
            i += 1
        i += 2
        var = ctx.getText()[i: -2]
        if name in self.variables:
            self.variables[name][1] = var
        else:
            raise Exception("You must declare the variable first")

    def visitCharAss(self, ctx: MiniJavaParser.CharAssContext):
        name = ctx.getText().split("=")
        if len(name[1]) != 4:
            raise Exception("You need to provide char")
        if name[0] in self.variables:
            self.variables[name[0]][1] = name[1][1:2]
        else:
            raise Exception("You must declare the variable first")

#endregion

#region loops
    def visitForloop(self, ctx:MiniJavaParser.ForloopContext):
        old = self.visit(ctx.decl)
        while self.visit(ctx.cond):
            tempdict = self.variables.copy()
            self.visit(ctx.body)
            self.visit(ctx.ass)
            self.variables = tempdict
        if len(old) == 1:
            del self.variables[old[0]]
            del self.tempVariables[old[0]]
        else:
            self.variables[old[0]][1] = old[1]
            del self.tempVariables[old[0]]


    def visitTempDeclaration(self, ctx:MiniJavaParser.TempDeclarationContext):
        name = ctx.getText().split("int")[1].split("=")
        if not name[0] in self.tempVariables:
            self.tempVariables[name[0]] = ["int", int(name[1][:-1])]
        else:
            raise Exception("Declared twice variable inside scope")
        if name[0] in self.variables:
            old = self.variables[name[0]][1]
            self.variables[name[0]][1] = int(name[1][0])
            return [name[0], old]
        else:
            self.variables[name[0]] = ["int", int(name[1][:-1])]
            return [name[0]]

    def visitWhileloop(self, ctx:MiniJavaParser.WhileloopContext):
        while self.visit(ctx.cond):
            tempdict = self.variables.copy()
            self.visit(ctx.body)
            self.variables = tempdict

#endregion

# region functions

    def visitFunction(self, ctx:MiniJavaParser.FunctionContext):
        # self.visit(self.functions[ctx.name.text][0])
        pass

    def visitFunction_call(self, ctx:MiniJavaParser.Function_callContext):
        pars = ctx.getText().split("(")[1].split(")")[0].split(",")
        print(pars)
        for i, v in enumerate(pars):
            print(type(self.visit()))
            print(self.functions[ctx.name.text][1][i])
            # print(str(type(v))==self.functions[ctx.name.text][1][i])
        self.visit(self.functions[ctx.name.text][2].body)

# endregion
    def dummy(self):
        pass