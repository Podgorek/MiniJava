grammar MiniJava;

prog:   (declaration | statement | function | function_call)* ;


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

declaration
    : 'int' VARIABLE ASSIGN INT SEMICOLON
    | 'float' VARIABLE ASSIGN FLOAT SEMICOLON
    | 'string' VARIABLE ASSIGN STRING SEMICOLON
    | 'bool' VARIABLE ASSIGN BOOL SEMICOLON
    | 'char' VARIABLE ASSIGN CHAR SEMICOLON
    | 'int' VARIABLE SEMICOLON
    | 'float' VARIABLE SEMICOLON
    | 'string' VARIABLE SEMICOLON
    | 'bool' VARIABLE SEMICOLON
    | 'char' VARIABLE SEMICOLON
    | 'int' VARIABLE ASSIGN 'input' '(' printable')' SEMICOLON
    | 'float' VARIABLE ASSIGN 'input' '(' printable')' SEMICOLON
    | 'string' VARIABLE ASSIGN 'input' '(' printable')' SEMICOLON
    | 'bool' VARIABLE ASSIGN 'input' '(' printable')' SEMICOLON
    | 'char' VARIABLE ASSIGN 'input' '(' printable')' SEMICOLON
    ;

statement
    :   '{' (statement)* '}'
    |   'if' '(' expression ')' statement ('else if' '(' expression')' statement)* ('else' statement)?
    |   'while' '(' expression ')' statement
    |   'for' '(' declaration expression SEMICOLON VARIABLE INC ')' statement
    |   VARIABLE '=' expression ';'
    |   expression ';'
    |   'return' expression ';'
    |   'print' '(' printable ')' SEMICOLON
    |   VARIABLE ASSIGN 'input' '(' printable ')' SEMICOLON
    |    'input' '(' printable ')' SEMICOLON
    ;

printable
    :   VARIABLE
    |   STRING
    |   INT
    |   CHAR
    |   BOOL
    |   FLOAT
    ;

expression
    :   expression '[' expression ']'
    |   expression '.' 'length'
    |   '!' expression
    |   'new' 'int' '[' expression ']'
    |   expression '+'  expression
    |   expression '-'  expression
    |   expression '*'  expression
    |   expression '/'  expression
    |   expression '%'  expression
    |   expression '<' expression
    |   expression '&&' expression
    |   expression '==' expression
    |   expression '>' expression
    |   expression '>=' expression
    |   expression '<=' expression
    |   '(' expression ')'
    |   expression'++'
    |   INT
    |   VARIABLE
    |   BOOL
    |   CHAR
    |   STRING
    |   FLOAT
    ;

function : VARIABLE '(' (('int'|'string'|'boolean'|'float'|'char') VARIABLE)* ')' '{' (expression|statement|'return' VARIABLE|INT|STRING|CHAR|FLOAT SEMICOLON)* '}';
function_call : VARIABLE '(' (TYPES VARIABLE)* ')' SEMICOLON;