# src/main.py

import sys
from lexer import tokenize, symbol_table  # Import the lexer and symbol table
from parser import parse_tokens  # Import the parser
from utils.ast_visualizer import ASTVisualizer
import os

file_path_for_symbol_table = os.path.join(os.getcwd(), "output/symbol_table.json")

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
        print(f"Type: {tok.type}, Value: {tok.value}, Line: {tok.lineno}, Column: {tok.column}")

    print("\n--- Syntax Analysis ---")
    ast = parse_tokens(tokens_list)

    print("\nAbstract Syntax Tree (AST):")
    print(ast)

    # Visualize the AST
    print("\n--- AST Visualization ---")
    visualizer = ASTVisualizer()
    visualizer.visualize(ast, output_filename='ast_output')  # You can change the filename as needed

    # Display the Symbol Table
    symbol_table.display()

    symbol_table.export_to_json(file_path_for_symbol_table)

if __name__ == '__main__':
    main()
