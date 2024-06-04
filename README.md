# TaskScript

TaskScript é uma linguagem simples para gerenciamento de lista de tarefas, projetada para facilitar a criação e manipulação de tarefas de forma eficiente.

## Características

- **Simplicidade**: TaskScript foi projetada com uma sintaxe simples e intuitiva, facilitando a criação e compreensão de scripts.
- **Flexibilidade**: Permite a criação, marcação e exibição de tarefas, além de suportar condicionais e loops para controle de fluxo.
- **Legibilidade**: A sintaxe foi projetada para ser legível e expressiva, facilitando a manutenção e compreensão do código.

## EBNF

```plaintext
PROGRAM             = { TASK_DECLARATION };
TASK_DECLARATION   = "TASK", IDENTIFIER, ":", STRING, [TASK_STATE];
TASK_STATE         = "DONE" | "UNDONE";
COMMAND             = MARK_COMMAND | DISPLAY_COMMAND | LOOP_COMMAND | CONDITIONAL_COMMAND;
MARK_COMMAND        = "MARK", IDENTIFIER, "AS", TASK_STATE;
DISPLAY_COMMAND     = "DISPLAY", IDENTIFIER;
LOOP_COMMAND        = "REPEAT", "FOR", "EACH", TASK_STATE, "\n", "{", { COMMAND }, "}";
CONDITIONAL_COMMAND = "IF", CONDITION, "\n", "{", { COMMAND }, "}", ["ELSE", "\n", "{", { COMMAND }, "}"];
CONDITION           = IDENTIFIER, ("IS" | "IS NOT"), TASK_STATE;
IDENTIFIER          = LETTER, { LETTER | DIGIT | "_" };
STRING              = '"', ({ LETTER | DIGIT | "_" }), '"';
NUMBER              = DIGIT, { DIGIT };
LETTER              = ( "a" | "..." | "z" | "A" | "..." | "Z" ) ;
DIGIT               = ( "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0" ) ;
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

3. **Loop para exibir todas as tarefas não concluídas uma vez**:

    ```plaintext
    TASK comprar_leite: "Comprar leite" DONE
    TASK lavar_carro: "Lavar o carro"
    TASK pagar_contas: "Pagar contas"

    REPEAT FOR EACH UNDONE TASK
        DISPLAY CURRENT TASK
    ```

4. **Loop para exibir todas as tarefas concluídas uma vez**:

    ```plaintext
    TASK comprar_leite: "Comprar leite" DONE
    TASK lavar_carro: "Lavar o carro"
    TASK pagar_contas: "Pagar contas"

    REPEAT FOR EACH DONE TASK
        DISPLAY CURRENT TASK
    ```

5. **Condicional para exibir uma tarefa apenas se outra estiver concluída**:

    ```plaintext
    TASK comprar_leite: "Comprar leite"
    TASK lavar_carro: "Lavar o carro"

    IF comprar_leite IS DONE
        DISPLAY lavar_carro
    ENDIF
    ```

## Contribuição

Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.
