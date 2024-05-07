%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
%}

// Definição dos tokens
%token MOVER PARA SE ENTAO FIM_CONDICIONAL ENQUANTO FACA FIM_LOOP VARIAVEL COORDENADA
%token REI RAINHA TORRE BISPO CAVALO PEAO NUMERO
%token OPERADOR OPERADOR_LOGICO

// Definição da union
%union {
    char* sval;
    int ival;
}

// Definição das regras gramaticais
%%

programa: instrucao { printf("Programa válido!\n"); }
        | programa instrucao { printf("Programa válido!\n"); }
        ;

instrucao: movimento
         | condicional
         | loop
         ;

movimento: MOVER peca PARA coordenada { printf("Movimento válido!\n"); }
         ;

condicional: SE condicao ENTAO FIM_CONDICIONAL { printf("Condicional válido!\n"); }
            ;

loop: ENQUANTO condicao FACA FIM_LOOP { printf("Loop válido!\n"); }
    ;

peca: REI | RAINHA | TORRE | BISPO | CAVALO | PEAO
    ;

coordenada: letra NUMERO
          ;

condicao: expressao operador_logico expressao
        ;

expressao: termo operador termo
         ;

termo: VARIAVEL | NUMERO | '(' expressao ')'
     ;

letra: 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h'
     ;

operador: '+' | '-' | '*' | '/'
        ;

operador_logico: "<=" | '<' | '>' | "==" | ">="
               ;

%%

// Função de tratamento de erro
void yyerror(const char *s) {
    fprintf(stderr, "Erro de sintaxe: %s\n", s);
}

// Função principal
int main(int argc, char *argv[]) {
    FILE *yyin;

    if (argc < 2) {
        fprintf(stderr, "Uso: %s <arquivo de entrada>\n", argv[0]);
        return 1;
    }

    yyin = fopen(argv[1], "r");
    if (!yyin) {
        perror(argv[1]);
        return 1;
    }

    yyparse();

    fclose(yyin);
    return 0;
}