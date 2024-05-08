// Generated from C:/Users/admin/IdeaProjects/projekt/.idea/MiniJava.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class MiniJavaParser extends Parser {
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
		INT=41, STRING=42, VARIABLE=43, BOOL=44, FLOAT=45, CHAR=46, NEWLINE=47;
	public static final int
		RULE_prog = 0, RULE_statement = 1, RULE_expression = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "statement", "expression"
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
			"VARIABLE", "BOOL", "FLOAT", "CHAR", "NEWLINE"
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

	@Override
	public String getGrammarFileName() { return "MiniJava.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MiniJavaParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(MiniJavaParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(MiniJavaParser.NEWLINE, i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MiniJavaListener ) ((MiniJavaListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MiniJavaListener ) ((MiniJavaListener)listener).exitProg(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MiniJavaVisitor ) return ((MiniJavaVisitor<? extends T>)visitor).visitProg(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(11);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 28587306517760L) != 0)) {
				{
				{
				setState(6);
				expression(0);
				setState(7);
				match(NEWLINE);
				}
				}
				setState(13);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(MiniJavaParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(MiniJavaParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode LPAREN() { return getToken(MiniJavaParser.LPAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(MiniJavaParser.RPAREN, 0); }
		public TerminalNode VARIABLE() { return getToken(MiniJavaParser.VARIABLE, 0); }
		public TerminalNode ASSIGN() { return getToken(MiniJavaParser.ASSIGN, 0); }
		public TerminalNode INT() { return getToken(MiniJavaParser.INT, 0); }
		public List<TerminalNode> SEMICOLON() { return getTokens(MiniJavaParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(MiniJavaParser.SEMICOLON, i);
		}
		public TerminalNode ADD_ASSIGN() { return getToken(MiniJavaParser.ADD_ASSIGN, 0); }
		public TerminalNode LBRACK() { return getToken(MiniJavaParser.LBRACK, 0); }
		public TerminalNode RBRACK() { return getToken(MiniJavaParser.RBRACK, 0); }
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MiniJavaListener ) ((MiniJavaListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MiniJavaListener ) ((MiniJavaListener)listener).exitStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MiniJavaVisitor ) return ((MiniJavaVisitor<? extends T>)visitor).visitStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		int _la;
		try {
			setState(70);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(14);
				match(LBRACE);
				setState(18);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 8796093026426L) != 0)) {
					{
					{
					setState(15);
					statement();
					}
					}
					setState(20);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(21);
				match(RBRACE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(22);
				match(T__0);
				setState(23);
				match(LPAREN);
				setState(24);
				expression(0);
				setState(25);
				match(RPAREN);
				setState(26);
				statement();
				setState(27);
				match(T__1);
				setState(28);
				statement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(30);
				match(T__2);
				setState(31);
				match(LPAREN);
				setState(32);
				expression(0);
				setState(33);
				match(RPAREN);
				setState(34);
				statement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(36);
				match(T__3);
				setState(37);
				match(LPAREN);
				setState(38);
				match(VARIABLE);
				setState(39);
				match(ASSIGN);
				setState(40);
				match(INT);
				setState(41);
				match(SEMICOLON);
				setState(42);
				expression(0);
				setState(43);
				match(SEMICOLON);
				setState(44);
				match(ADD_ASSIGN);
				setState(45);
				match(RPAREN);
				setState(46);
				statement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(48);
				match(VARIABLE);
				setState(49);
				match(ASSIGN);
				setState(50);
				expression(0);
				setState(51);
				match(SEMICOLON);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(53);
				match(VARIABLE);
				setState(54);
				match(LBRACK);
				setState(55);
				expression(0);
				setState(56);
				match(RBRACK);
				setState(57);
				match(ASSIGN);
				setState(58);
				expression(0);
				setState(59);
				match(SEMICOLON);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(61);
				match(T__4);
				setState(62);
				expression(0);
				setState(63);
				match(SEMICOLON);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(65);
				match(T__5);
				setState(66);
				match(LPAREN);
				setState(67);
				expression(0);
				setState(68);
				match(RPAREN);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(MiniJavaParser.NOT, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode LBRACK() { return getToken(MiniJavaParser.LBRACK, 0); }
		public TerminalNode RBRACK() { return getToken(MiniJavaParser.RBRACK, 0); }
		public TerminalNode INT() { return getToken(MiniJavaParser.INT, 0); }
		public TerminalNode BOOL() { return getToken(MiniJavaParser.BOOL, 0); }
		public TerminalNode VARIABLE() { return getToken(MiniJavaParser.VARIABLE, 0); }
		public TerminalNode LPAREN() { return getToken(MiniJavaParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(MiniJavaParser.RPAREN, 0); }
		public TerminalNode ADD() { return getToken(MiniJavaParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(MiniJavaParser.SUB, 0); }
		public TerminalNode MUL() { return getToken(MiniJavaParser.MUL, 0); }
		public TerminalNode LT() { return getToken(MiniJavaParser.LT, 0); }
		public TerminalNode AND() { return getToken(MiniJavaParser.AND, 0); }
		public TerminalNode EQUAL() { return getToken(MiniJavaParser.EQUAL, 0); }
		public TerminalNode DOT() { return getToken(MiniJavaParser.DOT, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MiniJavaListener ) ((MiniJavaListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MiniJavaListener ) ((MiniJavaListener)listener).exitExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MiniJavaVisitor ) return ((MiniJavaVisitor<? extends T>)visitor).visitExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				{
				setState(73);
				match(NOT);
				setState(74);
				expression(12);
				}
				break;
			case T__7:
				{
				setState(75);
				match(T__7);
				setState(76);
				match(T__8);
				setState(77);
				match(LBRACK);
				setState(78);
				expression(0);
				setState(79);
				match(RBRACK);
				}
				break;
			case INT:
				{
				setState(81);
				match(INT);
				}
				break;
			case BOOL:
				{
				setState(82);
				match(BOOL);
				}
				break;
			case VARIABLE:
				{
				setState(83);
				match(VARIABLE);
				}
				break;
			case LPAREN:
				{
				setState(84);
				match(LPAREN);
				setState(85);
				expression(0);
				setState(86);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(118);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(116);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(90);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(91);
						match(ADD);
						setState(92);
						expression(11);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(93);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(94);
						match(SUB);
						setState(95);
						expression(10);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(96);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(97);
						match(MUL);
						setState(98);
						expression(9);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(99);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(100);
						match(LT);
						setState(101);
						expression(8);
						}
						break;
					case 5:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(102);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(103);
						match(AND);
						setState(104);
						expression(7);
						}
						break;
					case 6:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(105);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(106);
						match(EQUAL);
						setState(107);
						expression(6);
						}
						break;
					case 7:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(108);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(109);
						match(LBRACK);
						setState(110);
						expression(0);
						setState(111);
						match(RBRACK);
						}
						break;
					case 8:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(113);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(114);
						match(DOT);
						setState(115);
						match(T__6);
						}
						break;
					}
					} 
				}
				setState(120);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 10);
		case 1:
			return precpred(_ctx, 9);
		case 2:
			return precpred(_ctx, 8);
		case 3:
			return precpred(_ctx, 7);
		case 4:
			return precpred(_ctx, 6);
		case 5:
			return precpred(_ctx, 5);
		case 6:
			return precpred(_ctx, 14);
		case 7:
			return precpred(_ctx, 13);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001/z\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002\u0002"+
		"\u0007\u0002\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000\n\b\u0000"+
		"\n\u0000\f\u0000\r\t\u0000\u0001\u0001\u0001\u0001\u0005\u0001\u0011\b"+
		"\u0001\n\u0001\f\u0001\u0014\t\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001G\b\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002Y\b\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0005\u0002u\b\u0002\n\u0002\f\u0002x\t\u0002"+
		"\u0001\u0002\u0000\u0001\u0004\u0003\u0000\u0002\u0004\u0000\u0000\u008c"+
		"\u0000\u000b\u0001\u0000\u0000\u0000\u0002F\u0001\u0000\u0000\u0000\u0004"+
		"X\u0001\u0000\u0000\u0000\u0006\u0007\u0003\u0004\u0002\u0000\u0007\b"+
		"\u0005/\u0000\u0000\b\n\u0001\u0000\u0000\u0000\t\u0006\u0001\u0000\u0000"+
		"\u0000\n\r\u0001\u0000\u0000\u0000\u000b\t\u0001\u0000\u0000\u0000\u000b"+
		"\f\u0001\u0000\u0000\u0000\f\u0001\u0001\u0000\u0000\u0000\r\u000b\u0001"+
		"\u0000\u0000\u0000\u000e\u0012\u0005\f\u0000\u0000\u000f\u0011\u0003\u0002"+
		"\u0001\u0000\u0010\u000f\u0001\u0000\u0000\u0000\u0011\u0014\u0001\u0000"+
		"\u0000\u0000\u0012\u0010\u0001\u0000\u0000\u0000\u0012\u0013\u0001\u0000"+
		"\u0000\u0000\u0013\u0015\u0001\u0000\u0000\u0000\u0014\u0012\u0001\u0000"+
		"\u0000\u0000\u0015G\u0005\r\u0000\u0000\u0016\u0017\u0005\u0001\u0000"+
		"\u0000\u0017\u0018\u0005\n\u0000\u0000\u0018\u0019\u0003\u0004\u0002\u0000"+
		"\u0019\u001a\u0005\u000b\u0000\u0000\u001a\u001b\u0003\u0002\u0001\u0000"+
		"\u001b\u001c\u0005\u0002\u0000\u0000\u001c\u001d\u0003\u0002\u0001\u0000"+
		"\u001dG\u0001\u0000\u0000\u0000\u001e\u001f\u0005\u0003\u0000\u0000\u001f"+
		" \u0005\n\u0000\u0000 !\u0003\u0004\u0002\u0000!\"\u0005\u000b\u0000\u0000"+
		"\"#\u0003\u0002\u0001\u0000#G\u0001\u0000\u0000\u0000$%\u0005\u0004\u0000"+
		"\u0000%&\u0005\n\u0000\u0000&\'\u0005+\u0000\u0000\'(\u0005\u0013\u0000"+
		"\u0000()\u0005)\u0000\u0000)*\u0005\u0010\u0000\u0000*+\u0003\u0004\u0002"+
		"\u0000+,\u0005\u0010\u0000\u0000,-\u0005%\u0000\u0000-.\u0005\u000b\u0000"+
		"\u0000./\u0003\u0002\u0001\u0000/G\u0001\u0000\u0000\u000001\u0005+\u0000"+
		"\u000012\u0005\u0013\u0000\u000023\u0003\u0004\u0002\u000034\u0005\u0010"+
		"\u0000\u00004G\u0001\u0000\u0000\u000056\u0005+\u0000\u000067\u0005\u000e"+
		"\u0000\u000078\u0003\u0004\u0002\u000089\u0005\u000f\u0000\u00009:\u0005"+
		"\u0013\u0000\u0000:;\u0003\u0004\u0002\u0000;<\u0005\u0010\u0000\u0000"+
		"<G\u0001\u0000\u0000\u0000=>\u0005\u0005\u0000\u0000>?\u0003\u0004\u0002"+
		"\u0000?@\u0005\u0010\u0000\u0000@G\u0001\u0000\u0000\u0000AB\u0005\u0006"+
		"\u0000\u0000BC\u0005\n\u0000\u0000CD\u0003\u0004\u0002\u0000DE\u0005\u000b"+
		"\u0000\u0000EG\u0001\u0000\u0000\u0000F\u000e\u0001\u0000\u0000\u0000"+
		"F\u0016\u0001\u0000\u0000\u0000F\u001e\u0001\u0000\u0000\u0000F$\u0001"+
		"\u0000\u0000\u0000F0\u0001\u0000\u0000\u0000F5\u0001\u0000\u0000\u0000"+
		"F=\u0001\u0000\u0000\u0000FA\u0001\u0000\u0000\u0000G\u0003\u0001\u0000"+
		"\u0000\u0000HI\u0006\u0002\uffff\uffff\u0000IJ\u0005\u0016\u0000\u0000"+
		"JY\u0003\u0004\u0002\fKL\u0005\b\u0000\u0000LM\u0005\t\u0000\u0000MN\u0005"+
		"\u000e\u0000\u0000NO\u0003\u0004\u0002\u0000OP\u0005\u000f\u0000\u0000"+
		"PY\u0001\u0000\u0000\u0000QY\u0005)\u0000\u0000RY\u0005,\u0000\u0000S"+
		"Y\u0005+\u0000\u0000TU\u0005\n\u0000\u0000UV\u0003\u0004\u0002\u0000V"+
		"W\u0005\u000b\u0000\u0000WY\u0001\u0000\u0000\u0000XH\u0001\u0000\u0000"+
		"\u0000XK\u0001\u0000\u0000\u0000XQ\u0001\u0000\u0000\u0000XR\u0001\u0000"+
		"\u0000\u0000XS\u0001\u0000\u0000\u0000XT\u0001\u0000\u0000\u0000Yv\u0001"+
		"\u0000\u0000\u0000Z[\n\n\u0000\u0000[\\\u0005 \u0000\u0000\\u\u0003\u0004"+
		"\u0002\u000b]^\n\t\u0000\u0000^_\u0005!\u0000\u0000_u\u0003\u0004\u0002"+
		"\n`a\n\b\u0000\u0000ab\u0005\"\u0000\u0000bu\u0003\u0004\u0002\tcd\n\u0007"+
		"\u0000\u0000de\u0005\u0015\u0000\u0000eu\u0003\u0004\u0002\bfg\n\u0006"+
		"\u0000\u0000gh\u0005\u001c\u0000\u0000hu\u0003\u0004\u0002\u0007ij\n\u0005"+
		"\u0000\u0000jk\u0005\u0018\u0000\u0000ku\u0003\u0004\u0002\u0006lm\n\u000e"+
		"\u0000\u0000mn\u0005\u000e\u0000\u0000no\u0003\u0004\u0002\u0000op\u0005"+
		"\u000f\u0000\u0000pu\u0001\u0000\u0000\u0000qr\n\r\u0000\u0000rs\u0005"+
		"\u0012\u0000\u0000su\u0005\u0007\u0000\u0000tZ\u0001\u0000\u0000\u0000"+
		"t]\u0001\u0000\u0000\u0000t`\u0001\u0000\u0000\u0000tc\u0001\u0000\u0000"+
		"\u0000tf\u0001\u0000\u0000\u0000ti\u0001\u0000\u0000\u0000tl\u0001\u0000"+
		"\u0000\u0000tq\u0001\u0000\u0000\u0000ux\u0001\u0000\u0000\u0000vt\u0001"+
		"\u0000\u0000\u0000vw\u0001\u0000\u0000\u0000w\u0005\u0001\u0000\u0000"+
		"\u0000xv\u0001\u0000\u0000\u0000\u0006\u000b\u0012FXtv";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}