# src/parser/grammar.py

# Grammar rules for the C language subset

# List of token names is required for PLY
tokens = [
    # Keywords
    'INT',
    'FLOAT',
    'IF',
    'ELSE',
    'WHILE',
    'RETURN',

    # Operators
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'ASSIGN',
    'LT',
    'GT',
    'LE',
    'GE',
    'EQ',
    'NE',

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
]

# Precedence rules to resolve ambiguities
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NE'),
    ('left', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'NOT'),
    ('right', 'UMINUS'),
)

# No additional rules are defined here; grammar rules will be in parser.py
