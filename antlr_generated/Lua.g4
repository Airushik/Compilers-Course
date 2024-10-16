grammar Lua;

options {
  backtrack=true;
}

chunk : (stat (';')?)* (laststat (';')?)?;

block : chunk;

stat :  varlist1 '=' explist1 | 
	functioncall | 
	'do' block 'end' | 
	'while' exp 'do' block 'end' | 
	'repeat' block 'until' exp | 
	'if' exp 'then' block ('elseif' exp 'then' block)* ('else' block)? 'end' | 
	'for' NAME '=' exp ',' exp (',' exp)? 'do' block 'end' | 
	'for' namelist 'in' explist1 'do' block 'end' | 
	'function' funcname funcbody | 
	'local' 'function' NAME funcbody | 
	'local' namelist ('=' explist1)? ;

laststat : 'return' (explist1)? | 'break';

funcname : NAME ('.' NAME)* (':' NAME)? ;

varlist1 : var (',' var)*;

namelist : NAME (',' NAME)*;

explist1 : (exp ',')* exp;

exp :  ('nil' | 'false' | 'true' | number | string | '...' | function | prefixexp | tableconstructor | unop exp) (binop exp)* ;

var: (NAME | '(' exp ')' varSuffix) varSuffix*;

prefixexp: varOrExp nameAndArgs* | functioncall;

functioncall: varOrExp nameAndArgs+;

varOrExp: var | '(' exp ')';

nameAndArgs: (':' NAME)? args;

varSuffix: nameAndArgs* ('[' exp ']' | '.' NAME);

args :  '(' (explist1)? ')' | tableconstructor | string ;

function : 'function' funcbody;

funcbody : '(' (parlist1)? ')' funcblock 'end';

funcchunk : (stat (';')?)* (laststat (';')?)?;

funcblock : funcchunk;

parlist1 : namelist (',' '...')? | '...';

tableconstructor : '{' (fieldlist)? '}';

fieldlist : field (fieldsep field)* (fieldsep)?;

field : '[' exp ']' '=' exp | NAME '=' exp | exp;

fieldsep : ',' | ';';

binop : '+' | '-' | '*' | '/' | '^' | '%' | '..' | 
		 '<' | '<=' | '>' | '>=' | '==' | '~=' | 
		 'and' | 'or';

unop : '-' | 'not' | '#';

number : INT | FLOAT | EXP | HEX;

string	: NORMALSTRING | CHARSTRING | LONGSTRING;


// LEXER

NAME	:('a'..'z'|'A'..'Z'|'_')(options{greedy=true;}:	'a'..'z'|'A'..'Z'|'_'|'0'..'9')*
	;

INT	: ('0'..'9')+;

FLOAT 	:INT '.' INT ;

EXP	: (INT| FLOAT) ('E'|'e') ('-')? INT;

HEX	:'0x' ('0'..'9'| 'a'..'f')+ ;

	

NORMALSTRING
    :  '"' ( EscapeSequence | ~('\\'|'"') )* '"' 
    ;

CHARSTRING
   :	'\'' ( EscapeSequence | ~('\''|'\\') )* '\''
   ;

LONGSTRING
	:	'['('=')*'[' ( EscapeSequence | ~('\\'|']') )* ']'('=')*']'
	;

fragment
EscapeSequence
    :   '\\' ('b'|'t'|'n'|'f'|'r'|'\''|'\\')
    |   UnicodeEscape
    |   OctalEscape
    ;
    
fragment
OctalEscape
    :   '\\' ('0'..'3') ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7')
    ;
    
fragment
UnicodeEscape
    :   '\\' 'u' HexDigit HexDigit HexDigit HexDigit
    ;
    
fragment
HexDigit : ('0'..'9'|'a'..'f'|'A'..'F') ;


COMMENT
    :   '--[[' ( options {greedy=false;} : . )* ']]' -> skip
    ;
    
LINE_COMMENT
    : '--' ~('\n'|'\r')* '\r'? '\n' -> skip
    ;
    
    
WS  :  (' '|'\t'|'\u000C') -> skip
    ;
    
NEWLINE	: ('\r')? '\n' -> skip
	;