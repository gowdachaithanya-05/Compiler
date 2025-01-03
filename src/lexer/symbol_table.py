# src/lexer/symbol_table.py

class Symbol:
    """Represents an identifier in the symbol table."""
    def __init__(self, name, token_type, lineno):
        self.name = name
        self.token_type = token_type
        self.lineno = lineno

    def __repr__(self):
        return f"Symbol(name='{self.name}', type='{self.token_type}', line={self.lineno})"

class SymbolTable:
    """Stores symbols collected during lexical analysis."""
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, token_type, lineno):
        if name not in self.symbols:
            self.symbols[name] = Symbol(name, token_type, lineno)
            print(f"Added to Symbol Table: {self.symbols[name]}")
        else:
            print(f"Symbol '{name}' already exists in the Symbol Table.")

    def display(self):
        print("\n--- Symbol Table ---")
        if not self.symbols:
            print("No symbols collected.")
        else:
            for symbol in self.symbols.values():
                print(f"{symbol}")
        print("---------------------\n")
