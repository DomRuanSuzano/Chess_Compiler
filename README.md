# TaskScript

TaskScript é uma linguagem simples para gerenciamento de lista de tarefas, projetada para facilitar a criação e manipulação de tarefas de forma eficiente.

## Características

- **Simplicidade**: TaskScript foi projetada com uma sintaxe simples e intuitiva, facilitando a criação e compreensão de scripts.
- **Flexibilidade**: Permite a criação, marcação e exibição de tarefas, além de suportar condicionais e loops para controle de fluxo.
- **Legibilidade**: A sintaxe foi projetada para ser legível e expressiva, facilitando a manutenção e compreensão do código.

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

3. **Exibir todas as tarefas não concluídas**:

    ```plaintext
    TASK pagar_contas: "Pagar contas"
    DISPLAY_ALL_UNDONE
    ```

4. **Loop para exibir todas as tarefas não concluídas uma vez**:

    ```plaintext
    TASK comprar_leite: "Comprar leite" DONE
    TASK lavar_carro: "Lavar o carro"
    TASK pagar_contas: "Pagar contas"

    REPEAT FOR EACH UNDONE TASK
        DISPLAY CURRENT TASK
    ```

5. **Loop para exibir todas as tarefas concluídas uma vez**:

    ```plaintext
    TASK comprar_leite: "Comprar leite" DONE
    TASK lavar_carro: "Lavar o carro"
    TASK pagar_contas: "Pagar contas"

    REPEAT FOR EACH DONE TASK
        DISPLAY CURRENT TASK
    ```
