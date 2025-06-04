parser grammar ASICParser;

options { tokenVocab=ASICLexer; }

prog
   : (line)*
   ;

line
   : (definition|statement) comment? ;

definition: define_def | config_def | const_def;

define_def: DEFINE define_name expression ;

config_def: CONFIG config_name configuration ;

const_def: CONST const_name const_expr ;

constant: HEXADECIMAL | DECIMAL ;

statement
   : lbl | (lbl? (instruction | (instruction COMMA instruction) | (instruction COMMA instruction COMMA instruction)))
   ;

instruction
   : sregop | operator;

sregop : asignment | arith;

asignment : sreg ASSIGN (expression | arg);

arith : (R0 PLUSPLUS) | (sreg MINUSMINUS) ;


operator
    : resultexpr ASSIGN (aluop | stdop) argument   # AluSpOp
    | resultexpr ASSIGN spcop                      # SpCopOp
    | spcop                                        # SpCopOnly
    ;

lbl
   : label COLON
   ;

label
   : IDENTIFIER
   ;


primary_expression: constant | define_name | LPAREN expression RPAREN ;

unary_expression
    :
    primary_expression
    |   unary_operator unary_expression
    ;

unary_operator
    :    PLUS | MINUS | TILDE | NEG
    ;

mulop
    : STAR | DIV | MOD
    ;

multiplicative_expression
    :   unary_expression (mulop unary_expression)*
    ;

addop
    : PLUS | MINUS
    ;

additive_expression
    :   multiplicative_expression (addop multiplicative_expression)*
    ;

relop
    : LABRACKET | RABRACKET | LEQUAL | GEQUAL
    ;

relational_expression
    :   additive_expression (relop additive_expression)*
    ;

eqop
    : EQUAL | NEQUAL
    ;

equality_expression
    :   relational_expression (eqop relational_expression)*
    ;

and_expression
    :   equality_expression ( AMP equality_expression)*
    ;

xor_expression
    :   and_expression (CARET and_expression)*
    ;

or_expression
    :   xor_expression (BAR xor_expression)*
    ;

logicaland_expression
    :   or_expression (AMPAMP or_expression)*
    ;

logicalor_expression
    :   logicaland_expression ( BARBAR logicaland_expression)*
    ;

expression
    :   constant
    |   logicalor_expression
    ;

configuration: conf_atom (PLUS conf_atom)* ;

conf_atom: conf_d | conf_c;

conf_d: vreg (LBRACE expression RBRACE)? (LSHIFT expression)?;
conf_c: const_name | const_expr ;

const_expr: SC LBRACKET expression RBRACKET (LSHIFT expression)? ;

op: PLUS | MINUS | STAR | DIV ;

define_name : IDENTIFIER ;

config_name : IDENTIFIER ;

const_name : IDENTIFIER ;

argument: LPAREN (config_name | configuration) RPAREN ;

resultexpr: output | ( LPAREN output (COMMA output)+ RPAREN );

sreg: R0 | R1 | R2 | R3 ;

arg: ARG0 | ARG1 | ARG2 | ARG3 ;

vreg: V1 | V1H | V2 | V3 | V4;

output: vreg | CMP | OUT ;

stdop: A1 | A4 | A5 | A128D | SD | DINV ;

aluop: ID | INV | AND | OR | XOR | NOT ;

spcop: GEN | EOP | WAIT LPAREN expression RPAREN | JNZ LPAREN sreg COMMA label RPAREN ;

//opcode : aluop | stdop | spcop;
//opcode : aluop | stdop ;

comment : LINE_COMMENT ;
