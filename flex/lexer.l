%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "parser.tab.h"
%}

%%

MOVER    { return MOVER; }
PARA     { return PARA; }
SE       { return SE; }
ENTAO    { return ENTAO; }
FIM_CONDICIONAL { return FIM_CONDICIONAL; }
ENQUANTO { return ENQUANTO; }
FACA     { return FACA; }
FIM_LOOP { return FIM_LOOP; }
[a-zA-Z_][a-zA-Z0-9_]* { yylval.sval = strdup(yytext); return VARIAVEL; }
[a-h][1-8] { yylval.sval = strdup(yytext); return COORDENADA; }
[0-9]+ { yylval.ival = atoi(yytext); return NUMERO; }
'+' | '-' | '*' | '/' { return OPERADOR; }
[ \t\n]    ; // Ignora espaços em branco e quebras de linha
.          { return yytext[0]; } // Retorna caracteres individuais como tokens

%%

int yywrap() {
    return 1;
}
