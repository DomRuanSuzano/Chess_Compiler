%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern void yyerror(const char *s);
extern int yylex(void);
%}

%token TASK DONE UNDONE MARK AS DISPLAY REPEAT FOR EACH IF ELSE IS IS_NOT STRING NUMBER IDENTIFIER NEWLINE END

%%
program : task_declaration
        | program task_declaration
        ;

task_declaration : TASK IDENTIFIER STRING task_state NEWLINE
                | TASK IDENTIFIER STRING NEWLINE
                | MARK IDENTIFIER AS task_state NEWLINE
                | DISPLAY IDENTIFIER NEWLINE
                | REPEAT FOR EACH task_state NEWLINE task_declaration
                | if
                | NEWLINE
                 ;

if : IF condition NEWLINE task_declaration END
   | IF condition NEWLINE task_declaration ELSE NEWLINE task_declaration END;

task_state : DONE
            | UNDONE
            ;

condition : IDENTIFIER IS task_state
            | IDENTIFIER IS_NOT task_state
            ;

%%
void yyerror(const char *s) {
    fprintf(stderr, "%s\n", s);
}

int main() {
    yyparse();
    return 0;
}
