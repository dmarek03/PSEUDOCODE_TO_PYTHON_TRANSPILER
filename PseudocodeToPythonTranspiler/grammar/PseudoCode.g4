grammar PseudoCode;

// Lexer rules (tokeny)
DECLARE: 'DECLARE';
INTEGER: 'INTEGER';
REAL: 'REAL';
CHAR: 'CHAR';
STRING: 'STRING';
BOOLEAN: 'BOOLEAN';
ARRAY: 'ARRAY';
OF: 'OF';
INPUT: 'INPUT';
OUTPUT: 'OUTPUT';
IF: 'IF';
THEN: 'THEN';
ELSE: 'ELSE';
AND: 'AND';
OR: 'OR';
NOT: 'NOT';
ENDIF: 'ENDIF';
CASE: 'CASE';
ENDCASE: 'ENDCASE';
ENDFUCTION: 'ENDFUNCTION';
ENDPROCEDURE:'ENDPROCEDURE';
OTHERWISE: 'OTHERWISE';
WHILE: 'WHILE';
DO: 'DO';
ENDWHILE: 'ENDWHILE';
FOR: 'FOR';
TO: 'TO';
STEP: 'STEP';
NEXT: 'NEXT';
REPEAT: 'REPEAT';
UNTIL: 'UNTIL';
CALL: 'CALL';
FUNCTION: 'FUNCTION';
PROCEDURE: 'PROCEDURE';
LENGTH: 'LENGTH';
LCASE: 'LCASE';
UCASE: 'UCASE';
SUBSTRING: 'SUBSTRING';
ROUND: 'ROUND';
RANDOM: 'RANDOM';
RETURN: 'RETURN';
RETURNS: 'RETURNS';
OPENFILE: 'OPENFILE';
READFILE: 'READFILE';
WRITEFILE: 'WRITEFILE';
CLOSEFILE: 'CLOSEFILE';
TRUE: 'TRUE';
FALSE: 'FALSE';
ONE_LINE_COMMENT: '//' ~[\r\n]*;
MULTIPLE_LINE_COMMENT: '***' .*? '***';
LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';
COLON: ':';
COMMA: ',';
SEMICOLON: ';';
ASSIGN: '←';
STRING_LITERAL: '"' ( . | '\\' . )*? '"';
CHAR_LITERAL: '\'' ( '\\' . | ~['\\] ) '\'';
NUMBER: [0-9]+;
REAL_NUMBER:'-'?[0-9]+'.'[0-9]+;
IDENTIFIER: [A-Z-a-z][a-zA-Z0-9]*;

WS: [ \t\r\n]+ -> skip;

program: statement_list;

statement_list
    : (statement)*;


statement
    : declaration
    | assignment
    | input
    | output
    | if_statement
    | case_statement
    | while_loop
    | for_loop
    | repeat_until_loop
    | procedure_call
    | function_call
    | user_function_definition
    | file_handling
    | return_statement
    | comment_statement;

return_statement
    : RETURN expression;


comment_statement
    : ONE_LINE_COMMENT
    | MULTIPLE_LINE_COMMENT;


declaration
    : DECLARE IDENTIFIER COLON data_type;

data_type
    : INTEGER
    | REAL
    | CHAR
    | STRING
    | BOOLEAN
    | ARRAY LBRACKET index_type RBRACKET OF data_type;

index_type
    :IDENTIFIER
    | NUMBER;

assignment
    : IDENTIFIER ASSIGN expression
    | IDENTIFIER LBRACKET expression RBRACKET ASSIGN expression;

cast
    : type LPAREN expression RPAREN
    ;


type
    : REAL
    | INTEGER
    | STRING
    | BOOLEAN
    ;

expression
    : additionExpression;

additionExpression
    : multiplicationExpression
    | additionExpression ('+' | '-') multiplicationExpression;

multiplicationExpression
    : primaryExpression
    | multiplicationExpression ('*' | '/') primaryExpression;

primaryExpression
    : cast
    | term
    | file_handling
    | IDENTIFIER LBRACKET expression RBRACKET
    | LPAREN expression RPAREN
    | 'DIV' LPAREN expression COMMA expression RPAREN
    | 'MOD' LPAREN expression COMMA expression RPAREN;



term
    : IDENTIFIER
    | literal
    | function_call;

literal
    : NUMBER
    | REAL_NUMBER
    | CHAR_LITERAL
    | STRING_LITERAL
    | TRUE
    | FALSE;

input
    : INPUT IDENTIFIER;

output
    : OUTPUT value_list;


value_list
    : expression (COMMA expression)*
    | STRING_LITERAL
    | CHAR_LITERAL;

if_statement
    : IF condition THEN statement_list ENDIF
    | IF condition THEN statement_list ELSE statement_list ENDIF;

condition
    : expression comparison_operator expression
    | condition AND condition
    | condition OR condition
    | NOT condition
    | LPAREN condition RPAREN
    | LBRACKET condition RBRACKET;

comparison_operator
    : '='
    | '<>'
    | '<'
    | '<='
    | '>'
    | '>=';

case_statement
    : CASE OF IDENTIFIER  case_list ENDCASE;

case_list
    : case (case)*;

case
    : literal COLON statement_list
    | OTHERWISE COLON statement_list;

while_loop
    : WHILE condition DO statement_list ENDWHILE;

for_loop
    : FOR IDENTIFIER ASSIGN expression TO expression (STEP expression)? statement_list NEXT IDENTIFIER;


repeat_until_loop
    : REPEAT statement_list UNTIL condition;

procedure_call
    : CALL IDENTIFIER LPAREN argument_list RPAREN;

user_function_definition
    : FUNCTION IDENTIFIER LPAREN parameter_list RPAREN RETURNS data_type statement_list ENDFUCTION
    | PROCEDURE IDENTIFIER LPAREN parameter_list RPAREN statement_list ENDPROCEDURE;

parameter_list
    : parameter (COMMA parameter)*;

parameter
    : IDENTIFIER COLON data_type;

function_call
    : user_function_call
    | builtin_function_call;

user_function_call
    : IDENTIFIER LPAREN argument_list RPAREN;

argument_list
    : expression (COMMA expression)*;

builtin_function_call
    : LENGTH LPAREN ( IDENTIFIER  | STRING_LITERAL | CHAR_LITERAL) RPAREN
    | LCASE LPAREN (IDENTIFIER  | STRING_LITERAL | CHAR_LITERAL) RPAREN
    | UCASE LPAREN (IDENTIFIER  | STRING_LITERAL | CHAR_LITERAL) RPAREN
    | SUBSTRING LPAREN (IDENTIFIER | STRING_LITERAL) COMMA NUMBER COMMA NUMBER COMMA? NUMBER? RPAREN
    | ROUND LPAREN expression COMMA expression RPAREN
    | RANDOM LPAREN RPAREN;


file_handling
    : OPENFILE STRING_LITERAL FOR file_mode
    | READFILE STRING_LITERAL COMMA IDENTIFIER
    | WRITEFILE STRING_LITERAL COMMA IDENTIFIER
    | CLOSEFILE STRING_LITERAL;

file_mode
    : 'READ'
    | 'WRITE';
