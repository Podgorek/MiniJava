from antlr4 import *
from MiniJavaParser import MiniJavaParser
from MiniJavaLexer import MiniJavaLexer
from projekt.idea.folder1.MiniJavaVisitor import MiniJavaVisitor
from MyVisitor import MyVisitor

inp = FileStream("test1.MiniJava")
lexer = MiniJavaLexer(inp)
stream = CommonTokenStream(lexer)
parser = MiniJavaParser(stream)
# parser.addParseListener(MiniJavaListener())
tree = parser.prog()
visitor = MyVisitor()
visitor.visit(tree)
