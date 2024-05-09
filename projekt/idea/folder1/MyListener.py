from MiniJavaListener import MiniJavaListener
from MiniJavaParser import MiniJavaParser
class MyListener(MiniJavaListener):

    def __init__(self):
        super().__init__()
        self.variables = {}

    # def exitIntDeclaration(self, ctx:MiniJavaParser.IntDeclarationContext):
    #     temp = ctx.getText().split("int")[1].split("=")
    #     if temp[0] in self.variables:
    #         raise Exception("Double declaration")
    #     self.variables[temp[0]] = ["int", int(temp[1][:-1])]

    def exitCharDeclaration(self, ctx:MiniJavaParser.CharDeclarationContext):
        temp = ctx.getText().split("char")[1].split("=")
        if temp[0] in self.variables:
            raise Exception("Double declaration")
        self.variables[temp[0]] = ["char", temp[1][:-1]]

    def exitStringDeclaration(self, ctx:MiniJavaParser.StringDeclarationContext):
        temp = ctx.getText().split("\"")
        if temp[0][6:-1] in self.variables:
            raise Exception("Double declaration")
        self.variables[temp[0][6:-1]] = ["string", temp[1]]

    # def exitFloatDeclaration(self, ctx:MiniJavaParser.FloatDeclarationContext):
    #     temp = ctx.getText().split("float")[1].split("=")
    #     if temp[0] in self.variables:
    #         raise Exception("Double declaration")
    #     self.variables[temp[0]] = ["float", float(temp[1][:-1])]

    def exitBoolDeclaration(self, ctx:MiniJavaParser.BoolDeclarationContext):
        temp = ctx.getText().split("bool")[1].split("=")
        if temp[0] in self.variables:
            raise Exception("Double declaration")
        self.variables[temp[0]] = ["bool", True if temp[1][:-1]=='true' else False]

    def exitArithmeticsIntDeclaration(self, ctx:MiniJavaParser.ArithmeticsIntDeclarationContext):
        pass

    def exitArithmeticsFloatDeclaration(self, ctx:MiniJavaParser.ArithmeticsFloatDeclarationContext):
        pass
