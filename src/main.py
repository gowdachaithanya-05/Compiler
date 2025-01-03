# src/main.py

import sys
from lexer import tokenize
from parser import parse

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_c_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        sys.exit(1)

    print("\n--- Lexical Analysis ---")
    tokens_list = tokenize(data)

    print("\nTokens:")
    for tok in tokens_list:
        print(f"Type: {tok.type}, Value: {tok.value}, Line: {tok.lineno}")

    print("\n--- Syntax Analysis ---")
    ast = parse(tokens_list)

    print("\nAbstract Syntax Tree (AST):")
    print(ast)

if __name__ == '__main__':
    main()
