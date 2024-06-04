%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "y.tab.h"

char* yyval;
%}

%option noyywrap
%option yylineno

TASK task
DONE done
UNDONE undone
MARK mark
AS as
DISPLAY display
REPEAT repeat
FOR for
EACH each
IF if
ELSE else
END end
IS is
IS_NOT is_not
STRING \"([^\\\"]|\\.)*\" 
NUMBER [0-9]+
IDENTIFIER [a-zA-Z_][a-zA-Z0-9_]*
NEWLINE \n

%%
"TASK"          { yyval = strdup(yytext); return TASK; }
"DONE"          { yyval = strdup(yytext); return DONE; }
"END"           { yyval = strdup(yytext); return END; }
"UNDONE"        { yyval = strdup(yytext); return UNDONE; }
"MARK"          { yyval = strdup(yytext); return MARK; }
"AS"            { yyval = strdup(yytext); return AS; }
"DISPLAY"       { yyval = strdup(yytext); return DISPLAY; }
"REPEAT"        { yyval = strdup(yytext); return REPEAT; }
"FOR"           { yyval = strdup(yytext); return FOR; }
"EACH"          { yyval = strdup(yytext); return EACH; }
"IF"            { yyval = strdup(yytext); return IF; }
"ELSE"          { yyval = strdup(yytext); return ELSE; }
"IS"            { yyval = strdup(yytext); return IS; }
"IS NOT"        { yyval = strdup(yytext); return IS_NOT; }
\"([^\\\"]|\\.)*\" { yyval = strdup(yytext); return STRING; }
[0-9]+          { yyval = strdup(yytext); return NUMBER; }
[a-zA-Z_][a-zA-Z0-9_]* { yyval = strdup(yytext); return IDENTIFIER; }
\n              { return NEWLINE; }
[ \t]           ; /* Ignorar espaços em branco */
.               { printf("Caractere não reconhecido: %s\n", yytext); }

%%
