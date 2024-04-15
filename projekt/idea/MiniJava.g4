grammar MiniJava;

prog:   (arithmetics | print | logical)* ;

LPAREN     : '(';
RPAREN     : ')';
LBRACE     : '{';
RBRACE     : '}';
LBRACK     : '[';
RBRACK     : ']';
SEMICOLON  : ';';
COMMA      : ',';
DOT        : '.';

ASSIGN         : '=';
GT             : '>';
LT             : '<';
NOT            : '!';
QUESTION       : '?';
EQUAL          : '==';
LE             : '<=';
GE             : '>=';
NOTEQUAL       : '!=';
AND            : '&&';
OR             : '||';
INC            : '++';
DEC            : '--';
ADD            : '+';
SUB            : '-';
MUL            : '*';
DIV            : '/';
MOD            : '%';
ADD_ASSIGN     : '+=';
SUB_ASSIGN     : '-=';
MUL_ASSIGN     : '*=';
DIV_ASSIGN     : '/=';
WS: [ \t\r\n]+ -> skip;

INT     : [0-9]+;
STRING  : '"'[a-zA-Z0-9_ ]+'"';
BOOL    : 'true' | 'false';
FLOAT   : ('0' '.' [0-9]+ | [1-9][0-9]* '.' [0-9]*) | ('0' '.' [0-9]*);
CHAR    : '\''[a-zA-Z0-9]'\'';
VARIABLE : [a-zA-Z]+;


arithmetics
    :   left=arithmetics op=('*'|'/'|'%') right=arithmetics   #opArithm
    |   left=arithmetics op=('+'|'-') right=arithmetics       #opArithm
    |   '(' arithmetics ')'                                   #parenArithm
    |   (INT | FLOAT)                                         #atomArithm
    ;


logical
    :   left=logical op='&&' right=logical                    #logicalAnd
    |   left=logical op='||' right=logical                    #logicalOr
    |   op = '!' logical                                      #logicalNot
    |   '(' logical ')'                                       #logicalParen
    |   BOOL                                                  #logicalAtom
    ;


print
    :   'print(' arithmetics ')' ';'                          #printArithmetics
    |   'print(' logical ')' ';'                                 #printLogical
    |   'print(' STRING ')' ';'                               #printString
    |   'print(' INT ')' ';'                                  #printInt
    |   'print(' FLOAT ')' ';'                                #printFloat
    |   'print(' BOOL ')' ';'                                 #printBool
    |   'print(' CHAR ')' ';'                                 #printChar
//    |   'print(' ((arithmetics|STRING|INT|FLOAT|BOOL|CHAR) '+')*(arithmetics|STRING|INT|FLOAT|BOOL|CHAR)');' #printMany
    ;