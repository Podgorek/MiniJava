// Generated from C:/Users/admin/IdeaProjects/projekt/.idea/MiniJava.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class MiniJavaLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		LPAREN=10, RPAREN=11, LBRACE=12, RBRACE=13, LBRACK=14, RBRACK=15, SEMICOLON=16, 
		COMMA=17, DOT=18, ASSIGN=19, GT=20, LT=21, NOT=22, QUESTION=23, EQUAL=24, 
		LE=25, GE=26, NOTEQUAL=27, AND=28, OR=29, INC=30, DEC=31, ADD=32, SUB=33, 
		MUL=34, DIV=35, MOD=36, ADD_ASSIGN=37, SUB_ASSIGN=38, MUL_ASSIGN=39, DIV_ASSIGN=40, 
		INT=41, STRING=42, VARIABLE=43, BOOL=44, FLOAT=45, CHAR=46;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMICOLON", 
			"COMMA", "DOT", "ASSIGN", "GT", "LT", "NOT", "QUESTION", "EQUAL", "LE", 
			"GE", "NOTEQUAL", "AND", "OR", "INC", "DEC", "ADD", "SUB", "MUL", "DIV", 
			"MOD", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "INT", 
			"STRING", "VARIABLE", "BOOL", "FLOAT", "CHAR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'else'", "'while'", "'for'", "'return'", "'print'", "'length'", 
			"'new'", "'int'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", 
			"'.'", "'='", "'>'", "'<'", "'!'", "'?'", "'=='", "'<='", "'>='", "'!='", 
			"'&&'", "'||'", "'++'", "'--'", "'+'", "'-'", "'*'", "'/'", "'%'", "'+='", 
			"'-='", "'*='", "'/='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "LPAREN", 
			"RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMICOLON", "COMMA", 
			"DOT", "ASSIGN", "GT", "LT", "NOT", "QUESTION", "EQUAL", "LE", "GE", 
			"NOTEQUAL", "AND", "OR", "INC", "DEC", "ADD", "SUB", "MUL", "DIV", "MOD", 
			"ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "INT", "STRING", 
			"VARIABLE", "BOOL", "FLOAT", "CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public MiniJavaLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MiniJava.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000.\u0109\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007"+
		"&\u0002\'\u0007\'\u0002(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007"+
		"+\u0002,\u0007,\u0002-\u0007-\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t"+
		"\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0016"+
		"\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c"+
		"\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001!\u0001!\u0001"+
		"\"\u0001\"\u0001#\u0001#\u0001$\u0001$\u0001$\u0001%\u0001%\u0001%\u0001"+
		"&\u0001&\u0001&\u0001\'\u0001\'\u0001\'\u0001(\u0004(\u00d7\b(\u000b("+
		"\f(\u00d8\u0001)\u0005)\u00dc\b)\n)\f)\u00df\t)\u0001*\u0001*\u0005*\u00e3"+
		"\b*\n*\f*\u00e6\t*\u0001+\u0001+\u0001+\u0001+\u0001+\u0001+\u0001+\u0001"+
		"+\u0001+\u0003+\u00f1\b+\u0001,\u0001,\u0001,\u0004,\u00f6\b,\u000b,\f"+
		",\u00f7\u0001,\u0004,\u00fb\b,\u000b,\f,\u00fc\u0001,\u0001,\u0005,\u0101"+
		"\b,\n,\f,\u0104\t,\u0003,\u0106\b,\u0001-\u0001-\u0000\u0000.\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f"+
		"\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f"+
		"\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017/\u0018"+
		"1\u00193\u001a5\u001b7\u001c9\u001d;\u001e=\u001f? A!C\"E#G$I%K&M\'O("+
		"Q)S*U+W,Y-[.\u0001\u0000\u0005\u0001\u000009\u0003\u000009AZaz\u0002\u0000"+
		"AZaz\u0004\u000009AZ__az\u0001\u000019\u0110\u0000\u0001\u0001\u0000\u0000"+
		"\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000"+
		"\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000"+
		"\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000"+
		"\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000"+
		"\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000"+
		"\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000"+
		"\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000"+
		"\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001"+
		"\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000"+
		"\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000"+
		"\u0000-\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000\u0000\u00001"+
		"\u0001\u0000\u0000\u0000\u00003\u0001\u0000\u0000\u0000\u00005\u0001\u0000"+
		"\u0000\u0000\u00007\u0001\u0000\u0000\u0000\u00009\u0001\u0000\u0000\u0000"+
		"\u0000;\u0001\u0000\u0000\u0000\u0000=\u0001\u0000\u0000\u0000\u0000?"+
		"\u0001\u0000\u0000\u0000\u0000A\u0001\u0000\u0000\u0000\u0000C\u0001\u0000"+
		"\u0000\u0000\u0000E\u0001\u0000\u0000\u0000\u0000G\u0001\u0000\u0000\u0000"+
		"\u0000I\u0001\u0000\u0000\u0000\u0000K\u0001\u0000\u0000\u0000\u0000M"+
		"\u0001\u0000\u0000\u0000\u0000O\u0001\u0000\u0000\u0000\u0000Q\u0001\u0000"+
		"\u0000\u0000\u0000S\u0001\u0000\u0000\u0000\u0000U\u0001\u0000\u0000\u0000"+
		"\u0000W\u0001\u0000\u0000\u0000\u0000Y\u0001\u0000\u0000\u0000\u0000["+
		"\u0001\u0000\u0000\u0000\u0001]\u0001\u0000\u0000\u0000\u0003`\u0001\u0000"+
		"\u0000\u0000\u0005e\u0001\u0000\u0000\u0000\u0007k\u0001\u0000\u0000\u0000"+
		"\to\u0001\u0000\u0000\u0000\u000bv\u0001\u0000\u0000\u0000\r|\u0001\u0000"+
		"\u0000\u0000\u000f\u0083\u0001\u0000\u0000\u0000\u0011\u0087\u0001\u0000"+
		"\u0000\u0000\u0013\u008b\u0001\u0000\u0000\u0000\u0015\u008d\u0001\u0000"+
		"\u0000\u0000\u0017\u008f\u0001\u0000\u0000\u0000\u0019\u0091\u0001\u0000"+
		"\u0000\u0000\u001b\u0093\u0001\u0000\u0000\u0000\u001d\u0095\u0001\u0000"+
		"\u0000\u0000\u001f\u0097\u0001\u0000\u0000\u0000!\u0099\u0001\u0000\u0000"+
		"\u0000#\u009b\u0001\u0000\u0000\u0000%\u009d\u0001\u0000\u0000\u0000\'"+
		"\u009f\u0001\u0000\u0000\u0000)\u00a1\u0001\u0000\u0000\u0000+\u00a3\u0001"+
		"\u0000\u0000\u0000-\u00a5\u0001\u0000\u0000\u0000/\u00a7\u0001\u0000\u0000"+
		"\u00001\u00aa\u0001\u0000\u0000\u00003\u00ad\u0001\u0000\u0000\u00005"+
		"\u00b0\u0001\u0000\u0000\u00007\u00b3\u0001\u0000\u0000\u00009\u00b6\u0001"+
		"\u0000\u0000\u0000;\u00b9\u0001\u0000\u0000\u0000=\u00bc\u0001\u0000\u0000"+
		"\u0000?\u00bf\u0001\u0000\u0000\u0000A\u00c1\u0001\u0000\u0000\u0000C"+
		"\u00c3\u0001\u0000\u0000\u0000E\u00c5\u0001\u0000\u0000\u0000G\u00c7\u0001"+
		"\u0000\u0000\u0000I\u00c9\u0001\u0000\u0000\u0000K\u00cc\u0001\u0000\u0000"+
		"\u0000M\u00cf\u0001\u0000\u0000\u0000O\u00d2\u0001\u0000\u0000\u0000Q"+
		"\u00d6\u0001\u0000\u0000\u0000S\u00dd\u0001\u0000\u0000\u0000U\u00e0\u0001"+
		"\u0000\u0000\u0000W\u00f0\u0001\u0000\u0000\u0000Y\u0105\u0001\u0000\u0000"+
		"\u0000[\u0107\u0001\u0000\u0000\u0000]^\u0005i\u0000\u0000^_\u0005f\u0000"+
		"\u0000_\u0002\u0001\u0000\u0000\u0000`a\u0005e\u0000\u0000ab\u0005l\u0000"+
		"\u0000bc\u0005s\u0000\u0000cd\u0005e\u0000\u0000d\u0004\u0001\u0000\u0000"+
		"\u0000ef\u0005w\u0000\u0000fg\u0005h\u0000\u0000gh\u0005i\u0000\u0000"+
		"hi\u0005l\u0000\u0000ij\u0005e\u0000\u0000j\u0006\u0001\u0000\u0000\u0000"+
		"kl\u0005f\u0000\u0000lm\u0005o\u0000\u0000mn\u0005r\u0000\u0000n\b\u0001"+
		"\u0000\u0000\u0000op\u0005r\u0000\u0000pq\u0005e\u0000\u0000qr\u0005t"+
		"\u0000\u0000rs\u0005u\u0000\u0000st\u0005r\u0000\u0000tu\u0005n\u0000"+
		"\u0000u\n\u0001\u0000\u0000\u0000vw\u0005p\u0000\u0000wx\u0005r\u0000"+
		"\u0000xy\u0005i\u0000\u0000yz\u0005n\u0000\u0000z{\u0005t\u0000\u0000"+
		"{\f\u0001\u0000\u0000\u0000|}\u0005l\u0000\u0000}~\u0005e\u0000\u0000"+
		"~\u007f\u0005n\u0000\u0000\u007f\u0080\u0005g\u0000\u0000\u0080\u0081"+
		"\u0005t\u0000\u0000\u0081\u0082\u0005h\u0000\u0000\u0082\u000e\u0001\u0000"+
		"\u0000\u0000\u0083\u0084\u0005n\u0000\u0000\u0084\u0085\u0005e\u0000\u0000"+
		"\u0085\u0086\u0005w\u0000\u0000\u0086\u0010\u0001\u0000\u0000\u0000\u0087"+
		"\u0088\u0005i\u0000\u0000\u0088\u0089\u0005n\u0000\u0000\u0089\u008a\u0005"+
		"t\u0000\u0000\u008a\u0012\u0001\u0000\u0000\u0000\u008b\u008c\u0005(\u0000"+
		"\u0000\u008c\u0014\u0001\u0000\u0000\u0000\u008d\u008e\u0005)\u0000\u0000"+
		"\u008e\u0016\u0001\u0000\u0000\u0000\u008f\u0090\u0005{\u0000\u0000\u0090"+
		"\u0018\u0001\u0000\u0000\u0000\u0091\u0092\u0005}\u0000\u0000\u0092\u001a"+
		"\u0001\u0000\u0000\u0000\u0093\u0094\u0005[\u0000\u0000\u0094\u001c\u0001"+
		"\u0000\u0000\u0000\u0095\u0096\u0005]\u0000\u0000\u0096\u001e\u0001\u0000"+
		"\u0000\u0000\u0097\u0098\u0005;\u0000\u0000\u0098 \u0001\u0000\u0000\u0000"+
		"\u0099\u009a\u0005,\u0000\u0000\u009a\"\u0001\u0000\u0000\u0000\u009b"+
		"\u009c\u0005.\u0000\u0000\u009c$\u0001\u0000\u0000\u0000\u009d\u009e\u0005"+
		"=\u0000\u0000\u009e&\u0001\u0000\u0000\u0000\u009f\u00a0\u0005>\u0000"+
		"\u0000\u00a0(\u0001\u0000\u0000\u0000\u00a1\u00a2\u0005<\u0000\u0000\u00a2"+
		"*\u0001\u0000\u0000\u0000\u00a3\u00a4\u0005!\u0000\u0000\u00a4,\u0001"+
		"\u0000\u0000\u0000\u00a5\u00a6\u0005?\u0000\u0000\u00a6.\u0001\u0000\u0000"+
		"\u0000\u00a7\u00a8\u0005=\u0000\u0000\u00a8\u00a9\u0005=\u0000\u0000\u00a9"+
		"0\u0001\u0000\u0000\u0000\u00aa\u00ab\u0005<\u0000\u0000\u00ab\u00ac\u0005"+
		"=\u0000\u0000\u00ac2\u0001\u0000\u0000\u0000\u00ad\u00ae\u0005>\u0000"+
		"\u0000\u00ae\u00af\u0005=\u0000\u0000\u00af4\u0001\u0000\u0000\u0000\u00b0"+
		"\u00b1\u0005!\u0000\u0000\u00b1\u00b2\u0005=\u0000\u0000\u00b26\u0001"+
		"\u0000\u0000\u0000\u00b3\u00b4\u0005&\u0000\u0000\u00b4\u00b5\u0005&\u0000"+
		"\u0000\u00b58\u0001\u0000\u0000\u0000\u00b6\u00b7\u0005|\u0000\u0000\u00b7"+
		"\u00b8\u0005|\u0000\u0000\u00b8:\u0001\u0000\u0000\u0000\u00b9\u00ba\u0005"+
		"+\u0000\u0000\u00ba\u00bb\u0005+\u0000\u0000\u00bb<\u0001\u0000\u0000"+
		"\u0000\u00bc\u00bd\u0005-\u0000\u0000\u00bd\u00be\u0005-\u0000\u0000\u00be"+
		">\u0001\u0000\u0000\u0000\u00bf\u00c0\u0005+\u0000\u0000\u00c0@\u0001"+
		"\u0000\u0000\u0000\u00c1\u00c2\u0005-\u0000\u0000\u00c2B\u0001\u0000\u0000"+
		"\u0000\u00c3\u00c4\u0005*\u0000\u0000\u00c4D\u0001\u0000\u0000\u0000\u00c5"+
		"\u00c6\u0005/\u0000\u0000\u00c6F\u0001\u0000\u0000\u0000\u00c7\u00c8\u0005"+
		"%\u0000\u0000\u00c8H\u0001\u0000\u0000\u0000\u00c9\u00ca\u0005+\u0000"+
		"\u0000\u00ca\u00cb\u0005=\u0000\u0000\u00cbJ\u0001\u0000\u0000\u0000\u00cc"+
		"\u00cd\u0005-\u0000\u0000\u00cd\u00ce\u0005=\u0000\u0000\u00ceL\u0001"+
		"\u0000\u0000\u0000\u00cf\u00d0\u0005*\u0000\u0000\u00d0\u00d1\u0005=\u0000"+
		"\u0000\u00d1N\u0001\u0000\u0000\u0000\u00d2\u00d3\u0005/\u0000\u0000\u00d3"+
		"\u00d4\u0005=\u0000\u0000\u00d4P\u0001\u0000\u0000\u0000\u00d5\u00d7\u0007"+
		"\u0000\u0000\u0000\u00d6\u00d5\u0001\u0000\u0000\u0000\u00d7\u00d8\u0001"+
		"\u0000\u0000\u0000\u00d8\u00d6\u0001\u0000\u0000\u0000\u00d8\u00d9\u0001"+
		"\u0000\u0000\u0000\u00d9R\u0001\u0000\u0000\u0000\u00da\u00dc\u0007\u0001"+
		"\u0000\u0000\u00db\u00da\u0001\u0000\u0000\u0000\u00dc\u00df\u0001\u0000"+
		"\u0000\u0000\u00dd\u00db\u0001\u0000\u0000\u0000\u00dd\u00de\u0001\u0000"+
		"\u0000\u0000\u00deT\u0001\u0000\u0000\u0000\u00df\u00dd\u0001\u0000\u0000"+
		"\u0000\u00e0\u00e4\u0007\u0002\u0000\u0000\u00e1\u00e3\u0007\u0003\u0000"+
		"\u0000\u00e2\u00e1\u0001\u0000\u0000\u0000\u00e3\u00e6\u0001\u0000\u0000"+
		"\u0000\u00e4\u00e2\u0001\u0000\u0000\u0000\u00e4\u00e5\u0001\u0000\u0000"+
		"\u0000\u00e5V\u0001\u0000\u0000\u0000\u00e6\u00e4\u0001\u0000\u0000\u0000"+
		"\u00e7\u00e8\u0005t\u0000\u0000\u00e8\u00e9\u0005r\u0000\u0000\u00e9\u00ea"+
		"\u0005u\u0000\u0000\u00ea\u00f1\u0005e\u0000\u0000\u00eb\u00ec\u0005f"+
		"\u0000\u0000\u00ec\u00ed\u0005a\u0000\u0000\u00ed\u00ee\u0005l\u0000\u0000"+
		"\u00ee\u00ef\u0005s\u0000\u0000\u00ef\u00f1\u0005e\u0000\u0000\u00f0\u00e7"+
		"\u0001\u0000\u0000\u0000\u00f0\u00eb\u0001\u0000\u0000\u0000\u00f1X\u0001"+
		"\u0000\u0000\u0000\u00f2\u00f3\u00050\u0000\u0000\u00f3\u00f5\t\u0000"+
		"\u0000\u0000\u00f4\u00f6\u0007\u0000\u0000\u0000\u00f5\u00f4\u0001\u0000"+
		"\u0000\u0000\u00f6\u00f7\u0001\u0000\u0000\u0000\u00f7\u00f5\u0001\u0000"+
		"\u0000\u0000\u00f7\u00f8\u0001\u0000\u0000\u0000\u00f8\u0106\u0001\u0000"+
		"\u0000\u0000\u00f9\u00fb\u0007\u0004\u0000\u0000\u00fa\u00f9\u0001\u0000"+
		"\u0000\u0000\u00fb\u00fc\u0001\u0000\u0000\u0000\u00fc\u00fa\u0001\u0000"+
		"\u0000\u0000\u00fc\u00fd\u0001\u0000\u0000\u0000\u00fd\u00fe\u0001\u0000"+
		"\u0000\u0000\u00fe\u0102\t\u0000\u0000\u0000\u00ff\u0101\u0007\u0000\u0000"+
		"\u0000\u0100\u00ff\u0001\u0000\u0000\u0000\u0101\u0104\u0001\u0000\u0000"+
		"\u0000\u0102\u0100\u0001\u0000\u0000\u0000\u0102\u0103\u0001\u0000\u0000"+
		"\u0000\u0103\u0106\u0001\u0000\u0000\u0000\u0104\u0102\u0001\u0000\u0000"+
		"\u0000\u0105\u00f2\u0001\u0000\u0000\u0000\u0105\u00fa\u0001\u0000\u0000"+
		"\u0000\u0106Z\u0001\u0000\u0000\u0000\u0107\u0108\u0007\u0001\u0000\u0000"+
		"\u0108\\\u0001\u0000\u0000\u0000\t\u0000\u00d8\u00dd\u00e4\u00f0\u00f7"+
		"\u00fc\u0102\u0105\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}