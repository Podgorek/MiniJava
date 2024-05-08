from antlr4 import *
from MiniJavaParser import MiniJavaParser
from MiniJavaLexer import MiniJavaLexer
from MyVisitor import MyVisitor
from MyListener import MyListener


inp = FileStream("test1.MiniJava")
lexer = MiniJavaLexer(inp)
stream = CommonTokenStream(lexer)
parser = MiniJavaParser(stream)
listener = MyListener()
parser.addParseListener(listener)
tree = parser.prog()
visitor = MyVisitor(listener.variables)
visitor.visit(tree)