from MiniJavaListener import MiniJavaListener
from MiniJavaParser import MiniJavaParser
import antlr4

class MyListener(MiniJavaListener):
    def __init__(self):
        self.functions = {}


    def exitFunction(self, ctx:MiniJavaParser.FunctionContext):
        name = ctx.name.text
        type = ctx.type_fun.text
        if name not in self.functions:
            arguments = ctx.getText().split("(")[1].split(")")[0].split(',')
            arguments_types = []
            for i in arguments:
                if i.startswith("int"):
                    arguments_types.append("int")
                elif i.startswith("string"):
                    arguments_types.append("string")
                elif i.startswith("char"):
                    arguments_types.append("char")
                elif i.startswith("float"):
                    arguments_types.append("float")
                elif i.startswith("bool"):
                    arguments_types.append("bool")
            self.functions[name] = [type, arguments_types, ctx]
        else:
            raise Exception("Function already exists")