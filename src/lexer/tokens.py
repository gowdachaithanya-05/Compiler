# src/lexer/tokens.py

# List of token names. This is always required
tokens = [
    # Operators
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'ASSIGN',

    # Delimiters
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COMMA',

    # Identifiers and literals
    'IDENTIFIER',
    'INT_LITERAL',
    'FLOAT_LITERAL',
    
    # Comparison Operators (to be added later)
    # Comparison Operators
    'LT',    # <
    'GT',    # >
    'LE',    # <=
    'GE',    # >=
    'EQ',    # ==
    'NE',    # !=

    # # Add Logical Operators
    # 'AND',    # &&
    # 'OR',     # ||
    # 'NOT',    # !

    # # String and Character Literals
    # 'STRING_LITERAL',
    # 'CHAR_LITERAL',



]

# Reserved words mapping
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'return': 'RETURN',
}

# Combine tokens and reserved words
tokens += list(reserved.values())
