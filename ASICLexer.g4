lexer grammar ASICLexer;

HEXADECIMAL:        '0' X HexDigit+ ;
DECIMAL:            Digit+ ;

fragment
Letter: ('a'..'z' | 'A'..'Z'| '_');

fragment
Digit: '0'..'9';

fragment
HexDigit : ('0'..'9'|'a'..'f'|'A'..'F') ;

fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];

R0: R '0' ;
R1: R '1' ;
R2: R '2' ;
R3: R '3' ;

ARG0: '$0' ;
ARG1: '$1' ;
ARG2: '$2' ;
ARG3: '$3' ;

V1: V '1' ;
V1H: V '1' H ;
V2: V '2' ;
V3: V '3' ;
V4: V '4' ;

DEFINE : D E F I N E;
CONFIG : C O N F I G;
CONST : C O N S T;

A1 : A '1';
A4 : A '4';
A5 : A '5';
A128D : A '128' D ;
DINV : D I N V ;
SD: D;
SC: C;

ID : I D ;
INV : I N V ;
AND : A N D ;
OR : O R ;
XOR : X O R ;
NOT : N O T ;

EOL
   : [\r\n] +
   ;

LPAREN: '(';

RPAREN: ')';

LBRACKET: '[';

LABRACKET: '<';

RBRACKET: ']';

RABRACKET: '>';

LBRACE: '{';

RBRACE: '}';

PLUS: '+';

MINUS: '-';

STAR: '*';

DIV: '/';

MOD: '%';

CARET: '^';

AMP : '&';
AMPAMP: '&&';
BAR : '|';
BARBAR: '||';

NEG: '!';

TILDE: '~';

ASSIGN: '=';

LSHIFT: '<<';

RSHIFT: '>>';

EQUAL: '==';

NEQUAL: '!=';

LEQUAL: '<=';

GEQUAL: '>=';

PLUSPLUS: '++';

MINUSMINUS: '--';

COMMA: ',';

COLON: ':';

SEMI: ';';

DOT: '.';

CMP: C M P ;
OUT: O U T ;
GEN: G E N ;
EOP: E O P ;
WAIT: W A I T;
JNZ: J N Z;


IDENTIFIER
    :   Letter (Letter|Digit)*
    ;

WS
   : (' ' | '\t' | '\n' | '\r') -> skip
   ;


LINE_COMMENT
   : ';' ~ ('\n' | '\r')* '\r'? '\n' -> skip
   ;
