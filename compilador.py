import re
import sys

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

class Tokenizer:
    def __init__(self, expression):
        self.source = expression
        self.pos = 0
        self.next = None
        self.tokens = re.findall(r'[-+*/(),=<>]+|\w+|"[^"]*"|\d+|\n', self.source)
        self.next_token()

    def next_token(self):
        if self.pos < len(self.tokens):
            valor = self.tokens[self.pos]
            self.pos += 1
            reservado = ["TASK", "MARK", "AS", "DISPLAY", "REPEAT", "FOR", "EACH", "IF", "IS", "IS NOT", "ELSE", "END", "DONE", "UNDONE"]
            if valor in reservado:
                self.next = Token(valor, valor)
            elif valor.startswith('"') and valor.endswith('"'):
                self.next = Token("STRING", valor[1:-1])
            elif valor.isdigit():
                self.next = Token("NUMBER", valor)
            elif re.match(r'^[a-zA-Z_]\w*$', valor):
                self.next = Token("IDENTIFIER", valor)
            elif valor == '\n':
                self.next = Token("NEWLINE", valor)
            else:
                raise ValueError(f"Token inválido: {valor}")
        else:
            self.next = Token("EOF", None)

class Parser:
    tokenizer = None

    @staticmethod
    def parser_state():
        if Parser.tokenizer.next.tipo in ["DONE", "UNDONE"]:
            state = Parser.tokenizer.next.valor
            Parser.tokenizer.next_token()
            return State(state)
        else:
            raise ValueError("Estado inválido")

    @staticmethod
    def parser_program():
        result = []
        while Parser.tokenizer.next.tipo != "EOF":
            result.append(Parser.parser_task())
        return Block(result)

    @staticmethod
    def parser_task():
        if Parser.tokenizer.next.tipo == "TASK":
            Parser.tokenizer.next_token()
            if Parser.tokenizer.next.tipo == "IDENTIFIER":
                name = Parser.tokenizer.next.valor
                Parser.tokenizer.next_token()
                if Parser.tokenizer.next.tipo == "STRING":
                    description = Parser.tokenizer.next.valor
                    Parser.tokenizer.next_token()
                    state = Parser.parser_state() if Parser.tokenizer.next.tipo in ["DONE", "UNDONE"] else State("UNDONE")
                    return Task(name, [description, state])
                else:
                    raise ValueError("Descrição inválida")
            else:
                raise ValueError("Nome inválido")
        elif Parser.tokenizer.next.tipo == "MARK":
            Parser.tokenizer.next_token()
            if Parser.tokenizer.next.tipo == "IDENTIFIER":
                name = Parser.tokenizer.next.valor
                Parser.tokenizer.next_token()
                if Parser.tokenizer.next.tipo == "AS":
                    Parser.tokenizer.next_token()
                    state = Parser.parser_state()
                    return Mark(name, [state])
                else:
                    raise ValueError("AS inválido")
            if Parser.tokenizer.next.tipo == "EACH":
                name = "EACH"
                Parser.tokenizer.next_token()
                if Parser.tokenizer.next.tipo == "AS":
                    Parser.tokenizer.next_token()
                    state = Parser.parser_state()
                    return Mark(name, [state])
            else:
                raise ValueError("Nome inválido")
        elif Parser.tokenizer.next.tipo == "DISPLAY":
            Parser.tokenizer.next_token()
            if Parser.tokenizer.next.tipo == "IDENTIFIER":
                name = Parser.tokenizer.next.valor
                Parser.tokenizer.next_token()
                return Display(name)
            elif Parser.tokenizer.next.tipo == "TASK":
                Parser.tokenizer.next_token()
                if Parser.tokenizer.next.tipo == "IDENTIFIER":
                    name = Parser.tokenizer.next.valor
                    Parser.tokenizer.next_token()
                    return Display(name)
                else:
                    raise ValueError("Nome inválido")
            else:
                raise ValueError("Nome inválido")
        elif Parser.tokenizer.next.tipo == "REPEAT":
            Parser.tokenizer.next_token()
            if Parser.tokenizer.next.tipo == "FOR":
                Parser.tokenizer.next_token()
                if Parser.tokenizer.next.tipo == "EACH":
                    Parser.tokenizer.next_token()
                    state = Parser.parser_state()
                    if Parser.tokenizer.next.tipo == "NEWLINE":
                        Parser.tokenizer.next_token()
                        tasks = []
                        while Parser.tokenizer.next.tipo != "END":
                            tasks.append(Parser.parser_task())
                        Parser.tokenizer.next_token()  # Consuming "END"
                        return Repeat([state, Block(tasks)])
                    else:
                        raise ValueError("Nova linha inválida")
                else:
                    raise ValueError("EACH inválido")
            else:
                raise ValueError("FOR inválido")
        elif Parser.tokenizer.next.tipo == "IF":
            Parser.tokenizer.next_token()
            condition = Parser.parser_condition()
            if Parser.tokenizer.next.tipo == "NEWLINE":
                Parser.tokenizer.next_token()
                tasks = []
                while Parser.tokenizer.next.tipo != "END" and Parser.tokenizer.next.tipo != "ELSE":
                    tasks.append(Parser.parser_task())
                if Parser.tokenizer.next.tipo == "ELSE":
                    Parser.tokenizer.next_token()
                    if Parser.tokenizer.next.tipo == "NEWLINE":
                        Parser.tokenizer.next_token()
                        else_tasks = []
                        while Parser.tokenizer.next.tipo != "END":
                            else_tasks.append(Parser.parser_task())
                        Parser.tokenizer.next_token()  # Consuming "END"
                        return If("IF", [condition, Block(tasks), Block(else_tasks)])
                    else:
                        raise ValueError("Nova linha inválida")
                else:
                    Parser.tokenizer.next_token()  # Consuming "END"
                    return If("IF", [condition, Block(tasks)])
            else:
                raise ValueError("Nova linha inválida")
        elif Parser.tokenizer.next.tipo == "NEWLINE":
            Parser.tokenizer.next_token()
            return NoOp()
        else:
            raise ValueError("Comando inválido")

    @staticmethod
    def parser_condition():
        if Parser.tokenizer.next.tipo == "IDENTIFIER":
            identifier = Parser.tokenizer.next.valor
            Parser.tokenizer.next_token()
            if Parser.tokenizer.next.tipo in ["IS", "IS NOT"]:
                op = Parser.tokenizer.next.valor
                Parser.tokenizer.next_token()
                state = Parser.parser_state()
                return Condition(op, [identifier, state])
            else:
                raise ValueError("Operador inválido")
        else:
            raise ValueError("Identificador inválido")
        
    @staticmethod
    def run(code, symbol_table):
        Parser.tokenizer = Tokenizer(code)
        program = Parser.parser_program()
        if Parser.tokenizer.next.tipo != "EOF":
            raise ValueError("Token inválido")
        return program.evaluate(symbol_table)

class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children if children is not None else []

    def evaluate(self, symbol_table):
        pass

class State(Node):
    def __init__(self, value):
        super().__init__(value=value)
    
    def evaluate(self, symbol_table):
        return self.value

class Condition(Node):
    def __init__(self, value, children):
        super().__init__(value=value, children=children)
    
    def evaluate(self, symbol_table):
        identifier, state = self.children
        if self.value == "IS":
            return symbol_table.get(identifier)[1] == state.evaluate(symbol_table)
        else:
            return symbol_table.get(identifier)[1] != state.evaluate(symbol_table)

class Task(Node):
    def __init__(self, name, children):
        super().__init__(value=name, children=children)
    
    def evaluate(self, symbol_table):
        description, state = self.children
        symbol_table.update(self.value, (description, state.evaluate(symbol_table)))

class Mark(Node):
    def __init__(self, name, children):
        super().__init__(value=name, children=children)

    def evaluate(self, symbol_table):
        if self.value == "EACH":
            for name, (description, task_state) in symbol_table.table.items():
                symbol_table.update(name, (description, self.children[0].evaluate(symbol_table)))
        else:
            state = self.children[0].evaluate(symbol_table)
            symbol_table.update(self.value, (symbol_table.get(self.value)[0], state))

class Display(Node):
    def __init__(self, value):
        super().__init__(value=value)
    
    def evaluate(self, symbol_table):
        print(symbol_table.get(self.value))

class Repeat(Node):
    def __init__(self, children):
        super().__init__(children=children)
    
    def evaluate(self, symbol_table):
        state = self.children[0].evaluate(symbol_table)
        block = self.children[1]
        for name, (description, task_state) in symbol_table.table.items():
            if task_state == state:
                block.evaluate(symbol_table)

class If(Node):
    def __init__(self, value, children):
        super().__init__(value=value, children=children)

    def evaluate(self, symbol_table):
        condition = self.children[0]
        if condition.evaluate(symbol_table):
            self.children[1].evaluate(symbol_table)
        elif len(self.children) > 2:
            self.children[2].evaluate(symbol_table)

class Block(Node):
    def __init__(self, children):
        super().__init__(children=children)

    def evaluate(self, symbol_table):
        for child in self.children:
            child.evaluate(symbol_table)

class NoOp(Node):
    def __init__(self):
        super().__init__()

    def evaluate(self, symbol_table):
        pass

class SymbolTable:
    def __init__(self):
        self.table = {}

    def create(self, name):
        if name not in self.table:
            self.table[name] = None
        else:
            raise ValueError("Variável já existe")
    
    def update(self, name, value):
        self.table[name] = value
    
    def get(self, name):
        if name not in self.table:
            raise ValueError("Variável não existe")
        return self.table[name]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 compilador.py <file>")
        sys.exit(1)
    try:
        with open(sys.argv[1], "r") as file:
            code = file.read()
        symbol_table = SymbolTable()
        Parser.run(code, symbol_table)
    
    except Exception as e:
        print(e)
        sys.exit(1)
