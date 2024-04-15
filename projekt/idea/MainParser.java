import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.ParseTree;

//public class MainParser {
//    public static void main(String[] args) throws Exception {
//        // Tworzenie strumienia znaków z pliku
//        CharStream in = CharStreams.fromFileName("C:/Users/admin/IdeaProjects/proba1/src/main/java/org/example/test.cc");
//
//        // Tworzenie leksera na podstawie strumienia znaków
//        ExprLexer lexer = new ExprLexer(in);
//
//        // Tworzenie strumienia tokenów na podstawie leksera
//        CommonTokenStream tokens = new CommonTokenStream(lexer);
//
//        // Tworzenie parsera na podstawie strumienia tokenów
//        ExprParser parser = new ExprParser(tokens);
//
//        // Pobranie drzewa parsowania
//        ExprParser.ExprContext parseTree = parser.expr();
//
//        // Wyświetlenie drzewa parsowania
//        System.out.println(parseTree.toStringTree());
//    }
//}
import org.antlr.v4.runtime.*;

public class SimpleLangInterpreter extends SimpleLangBaseListener {
    @Override
    public void enterPrintStatement(SimpleLangParser.PrintStatementContext ctx) {
        String arg = ctx.expression().getText();
        System.out.println(arg);
    }

    public static void main(String[] args) throws Exception {
        String input = "print("hello world");";
        CharStream inputStream = CharStreams.fromString(input);
        SimpleLangLexer lexer = new SimpleLangLexer(inputStream);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        SimpleLangParser parser = new SimpleLangParser(tokens);

        ParseTreeWalker walker = new ParseTreeWalker();
        SimpleLangInterpreter interpreter = new SimpleLangInterpreter();
        walker.walk(interpreter, parser.program());
        chuj

    }
}