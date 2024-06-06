grammar MiniJava;

prog:   (arithmetics | print | logical | declaration | conditionals
                     | assignments | forloop | whileloop | function_call | function)+ ;


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
IF             : 'if';
WS: [ \t\r\n]+ -> skip;

INT     : [0-9]+;
STRING  : '"'[a-zA-Z0-9_ =]+'"';
BOOL    : 'true' | 'false';
FLOAT   : ('0' '.' [0-9]+ | [1-9][0-9]* '.' [0-9]*) | ('0' '.' [0-9]*);
CHAR    : '\''[a-zA-Z0-9]'\'';
VARIABLE : [a-zA-Z]+;


function_call
    : name = VARIABLE '(' ((arithmetics|logical|STRING|CHAR|VARIABLE) (','(arithmetics|logical|STRING|CHAR|VARIABLE))*)? ')' ';'
    ;

function
    : type_fun=('void'|'bool'|'string'|'float'|'int'|'char') name=VARIABLE'(' (('bool'|'string'|'float'|'int'|'char') arg_name=VARIABLE (','('bool'|'string'|'float'|'int'|'char') arg_name=VARIABLE)*)? ')''{' (body=prog|ret=return)+ '}'
    ;

declaration
    : 'char' VARIABLE '=' CHAR ';'                            #charDeclaration
    | 'string' VARIABLE '=' STRING ';'                        #stringDeclaration
    | 'bool' VARIABLE '=' expr=logical ';'                    #logicalDeclaration
    | 'int' VARIABLE '=' expr=arithmetics ';'                 #arithmeticsIntDeclaration
    | 'float' VARIABLE '=' expr=arithmetics ';'               #arithmeticsFloatDeclaration
    ;

tempDeclaration
    : 'int' VARIABLE '=' INT ';'
    ;

assignments
    : VARIABLE '=' expr = arithmetics ';'                     #arithmeticsAss
    | VARIABLE '=' expr = logical ';'                         #logicalAss
    | VARIABLE '=' STRING';'                                  #stringAss
    | VARIABLE '=' CHAR ';'                                   #charAss
    ;

assignmentsFor
    : VARIABLE '=' expr = arithmetics                         #arithmeticsAssFor
    ;

arithmetics
    :   left=arithmetics op=('*'|'/'|'%') right=arithmetics   #opArithm
    |   left=arithmetics op=('+'|'-') right=arithmetics       #opArithm
    |   '(' arithmetics ')'                                   #parenArithm
    |   (INT | FLOAT | VARIABLE)                              #atomArithm
    ;


logical
    :   left=logical op='&&' right=logical                    #logicalAnd
    |   left=logical op='||' right=logical                    #logicalOr
    |   left=logical op='==' right=logical                    #logicalEquals
    |   left=logical op='!=' right=logical                    #logicalNotEquals
    |   left=arithmetics op='==' right=arithmetics            #arithmeticsEquals
    |   left=arithmetics op='!=' right=arithmetics            #arithmeticsNotEquals
    |   left=arithmetics op='<' right=arithmetics             #arithmeticsSmaller
    |   left=arithmetics op='<=' right=arithmetics            #arithmeticsSmallerEquals
    |   left=arithmetics op='>' right=arithmetics             #arithmeticsBigger
    |   left=arithmetics op='>=' right=arithmetics            #arithmeticsBiggerEquals
    |   op = '!' logical                                      #logicalNot
    |   '(' logical ')'                                       #logicalParen
    |   (BOOL | VARIABLE)                                     #logicalAtom
    ;

print
    :   'print(' VARIABLE ')' ';'                             #printVariable
    |   'print(' STRING ')' ';'                               #printString
    |   'print(' INT ')' ';'                                  #printInt
    |   'print(' FLOAT ')' ';'                                #printFloat
    |   'print(' BOOL ')' ';'                                 #printBool
    |   'print(' CHAR ')' ';'                                 #printChar
    |   'print(' logical ')' ';'                              #printLogical
    |   'print(' arithmetics ')' ';'                          #printArithmetics
    ;

conditionals
    :  'if' '(' cond=logical ')' '{' body=prog '}' (moreConditions=conditionalsExtend)?   #startIf
    ;

conditionalsExtend
    :  'else if' '(' cond=logical ')' '{' body=prog '}' (moreConditions=conditionalsExtend)?                #elif
    |  'else' '{' body=prog '}'                                               #else
    ;

whileloop
    : 'while' '(' cond=logical ')' '{' body=prog '}'
    ;

forloop
    : 'for' '(' decl=tempDeclaration cond=logical ';' ass=assignmentsFor ')' '{' body = prog '}'
    ;

return
    : 'return' expr=VARIABLE ';'                              #returnVariable
    | 'return' expr=CHAR ';'                                  #returnChar
    | 'return' expr=STRING';'                                 #returnString
    | 'return' expr=arithmetics';'                            #returnArtihmetics
    | 'return' expr=logical ';'                               #returnLogical
    ;


//function
//    : ('bool'|'string'|'float'|'int'|'char') name=VARIABLE'(' (((('bool'|'string'|'float'|'int'|'char') VARIABLE) (','('bool'|'string'|'float'|'int'|'char') VARIABLE)*) | ' ')  ')''{' (body=prog|ret=return)+ '}'
//    ;