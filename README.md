# Linguagem de Programação para Simulação de Xadrez

Esta é uma linguagem de programação simples criada para simular jogos de xadrez através de comandos de texto. Ela foi desenvolvida como parte de um projeto de aprendizado e tem como objetivo proporcionar uma experiência acessível e educativa para programadores interessados em explorar os fundamentos da linguagem de programação e a lógica por trás do jogo de xadrez.

## Funcionalidades Principais

- **Movimentação de Peças**: Os jogadores podem mover as peças no tabuleiro através de comandos específicos.
- **Condicionais e Loops**: A linguagem suporta construções como condicionais (se-então-senão) e loops (enquanto) para controle de fluxo.
- **Variáveis e Atribuições**: Os jogadores podem declarar variáveis e atribuir valores a elas para armazenar informações durante o jogo.
- **Chamadas de Funções**: Os jogadores podem definir e chamar funções para reutilizar blocos de código.

## Exemplo de Uso

```python
# Movimento do cavalo para a coordenada b3
MOVER cavalo PARA b3

# Condicional para verificar se o rei está em xeque
SE CONDICAO ENTAO
    # Bloco de instruções
FIM_CONDICIONAL

# Loop para realizar uma série de movimentos
ENQUANTO CONDICAO FACA
    # Bloco de instruções
FIM_LOOP
```

## Gramática EBNF

```python
programa           ::= { instrucao } ;

instrucao          ::= movimento
                     | condicional
                     | loop
                     | declaracao
                     | atribuicao
                     | chamada_funcao
                     | RETORNAR expressao ;

movimento          ::= MOVER peca PARA coordenada ;

condicional        ::= SE condicao ENTAO bloco_instrucoes ( SENAO bloco_instrucoes )? FIM_CONDICIONAL ;

loop               ::= ENQUANTO condicao faca bloco_instrucoes FIM_LOOP ;

declaracao         ::= tipo VARIAVEL ;

atribuicao         ::= VARIAVEL = expressao ;

chamada_funcao     ::= NOME_FUNCAO '(' parametros ')' ;

parametros         ::= expressao { ',' expressao } ;

bloco_instrucoes   ::= '{' programa '}' ;

expressao          ::= termo { operador termo } ;

termo              ::= VARIAVEL | NUMERO | '(' expressao ')' ;

condicao           ::= expressao operador_logico expressao ;

tipo               ::= INTEIRO | TEXTO | BOOLEANO ;

peca               ::= REI | RAINHA | TORRE | BISPO | CAVALO | PEAO ;

coordenada         ::= letra numero ;

letra              ::= 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' ;

numero             ::= '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' ;

operador           ::= '+' | '-' | '*' | '/' ;

operador_logico    ::= '==' | '!=' | '>' | '<' | '>=' | '<=' ;

INTEIRO            ::= "inteiro" ;
TEXTO              ::= "texto" ;
BOOLEANO           ::= "booleano" ;
REI                ::= "rei" ;
RAINHA             ::= "rainha" ;
TORRE              ::= "torre" ;
BISPO              ::= "bispo" ;
CAVALO             ::= "cavalo" ;
PEAO               ::= "peao" ;
VARIAVEL           ::= [a-zA-Z_][a-zA-Z0-9_]* ;
NOME_FUNCAO        ::= [a-zA-Z_][a-zA-Z0-9_]* ;
NUMERO             ::= [0-9]+ ;
```
