# TaskScript

TaskScript é uma linguagem simples para gerenciamento de lista de tarefas, projetada para facilitar a criação e manipulação de tarefas de forma eficiente.

## Características

- **Simplicidade**: TaskScript foi projetada com uma sintaxe simples e intuitiva, facilitando a criação e compreensão de scripts.
- **Flexibilidade**: Permite a criação, marcação e exibição de tarefas, além de suportar condicionais e loops para controle de fluxo.
- **Legibilidade**: A sintaxe foi projetada para ser legível e expressiva, facilitando a manutenção e compreensão do código.

## EBNF

```plaintext
PROGRAM             = { TASK_DECLARATION, NEWLINE };
TASK_DECLARATION   = "TASK", IDENTIFIER, STRING, [TASK_STATE]
                    | "MARK", IDENTIFIER, "AS", TASK_STATE
                    | "DISPLAY", IDENTIFIER
                    | "REPEAT", "FOR", "EACH", TASK_STATE, NEWLINE, { TASK_DECLARATION }, "END"
                    | "IF", CONDITION, NEWLINE, { COMMAND }, ["ELSE", NEWLINE, { TASK_DECLARATION }], "END"
                    | NEWLINE
;
TASK_STATE         = "DONE" | "UNDONE";
CONDITION           = IDENTIFIER, ("IS" | "IS NOT"), TASK_STATE;
IDENTIFIER          = LETTER, { LETTER | DIGIT | "_" };
STRING              = '"', ({ LETTER | DIGIT | "_" }), '"';
NUMBER              = DIGIT, { DIGIT };
LETTER              = ( "a" | "..." | "z" | "A" | "..." | "Z" ) ;
DIGIT               = ( "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0" ) ;
NEWLINE             = "\n";
```

## Exemplos de Uso

Aqui estão alguns exemplos de como usar o TaskScript:

1. **Marcar uma tarefa como concluída**:

    ```plaintext
    TASK comprar_leite: "Comprar leite"
    MARK comprar_leite AS DONE
    ```

2. **Exibir uma tarefa específica**:

    ```plaintext
    TASK lavar_carro: "Lavar o carro"
    DISPLAY lavar_carro
    ```

3. **Loop para marcar todas as tarefas concluídas de uma vez**:

    ```plaintext
    TASK comprar_leite "Comprar leite" DONE
    TASK lavar_carro "Lavar o carro"
    TASK pagar_contas "Pagar contas"
    
    REPEAT FOR EACH UNDONE
        MARK EACH AS DONE
    END

    ```

4. **Loop para marcar todas as tarefas não concluídas de uma vez**:

    ```plaintext
    TASK comprar_leite "Comprar leite" DONE
    TASK lavar_carro "Lavar o carro"
    TASK pagar_contas "Pagar contas" DONE
    
    REPEAT FOR EACH DONE
        MARK EACH AS UNDONE
    END
    ```

5. **Condicional para exibir uma tarefa apenas se outra estiver concluída**:

    ```plaintext
    TASK comprar_leite: "Comprar leite"
    TASK lavar_carro: "Lavar o carro"

    IF comprar_leite IS DONE
        DISPLAY lavar_carro
    END
    ```

## Contribuição

Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.
