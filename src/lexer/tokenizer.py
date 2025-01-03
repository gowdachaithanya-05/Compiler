# src/lexer/tokenizer.py

import ply.lex as lex
from .tokens import tokens, reserved

# Regular expression rules for simple tokens
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_MULTIPLY   = r'\*'
t_DIVIDE     = r'/'
t_ASSIGN     = r'='
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'
t_SEMICOLON  = r';'
t_COMMA      = r','

# Comparison Operators
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'

# # Logical Operators
# t_AND = r'&&'
# t_OR  = r'\|\|'
# t_NOT = r'!'



# A regular expression rule with some action code
def t_FLOAT_LITERAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT_LITERAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Identifier (variable names, function names)
def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Define a rule for newlines to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Comment handling (C-style single-line and multi-line)
def t_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass  # Ignore comments

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Function to tokenize input data
def tokenize(data):
    lexer.input(data)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append(tok)
    return tokens_list


# def t_STRING_LITERAL(t):
#     r'\"([^\\\n]|(\\.))*?\"'
#     t.value = t.value[1:-1]  # Remove quotes
#     return t

# def t_CHAR_LITERAL(t):
#     r'\'([^\\\n]|(\\.))\''
#     t.value = t.value[1:-1]  # Remove quotes
#     return t
