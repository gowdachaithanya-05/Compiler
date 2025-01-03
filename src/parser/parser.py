# src/parser/parser.py

import ply.yacc as yacc
from lexer.tokenizer import tokens  # Import tokens from lexer
from .ast_nodes import *

# Precedence rules to resolve ambiguities
precedence = (
    ('left', 'EQ', 'NE'),
    ('left', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# Define the grammar rules

def p_program(p):
    """program : declarations"""
    p[0] = Program(p[1])

def p_declarations(p):
    """declarations : declarations declaration
                    | declaration"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_declaration(p):
    """declaration : var_declaration
                   | func_declaration"""
    p[0] = p[1]

def p_var_declaration(p):
    """var_declaration : type_specifier IDENTIFIER SEMICOLON
                       | type_specifier IDENTIFIER ASSIGN expression SEMICOLON"""
    if len(p) == 4:
        p[0] = VariableDeclaration(var_type=p[1], name=p[2])
    else:
        p[0] = VariableDeclaration(var_type=p[1], name=p[2], initializer=p[4])

def p_type_specifier(p):
    """type_specifier : INT
                      | FLOAT"""
    p[0] = p[1]

def p_func_declaration(p):
    """func_declaration : type_specifier IDENTIFIER LPAREN params RPAREN compound_stmt"""
    p[0] = FunctionDeclaration(return_type=p[1], name=p[2], params=p[4], body=p[6])

def p_params(p):
    """params : param_list
              | empty"""
    p[0] = p[1]

def p_param_list(p):
    """param_list : param_list COMMA param
                  | param"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_param(p):
    """param : type_specifier IDENTIFIER"""
    p[0] = VariableDeclaration(var_type=p[1], name=p[2])

def p_compound_stmt(p):
    """compound_stmt : LBRACE stmt_list RBRACE"""
    p[0] = CompoundStatement(statements=p[2])

def p_stmt_list(p):
    """stmt_list : stmt_list statement
                 | empty"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []

def p_statement(p):
    """statement : expr_stmt
                 | var_declaration
                 | compound_stmt
                 | if_stmt
                 | return_stmt"""
    p[0] = p[1]

def p_if_stmt(p):
    """if_stmt : IF LPAREN expression RPAREN statement
               | IF LPAREN expression RPAREN statement ELSE statement"""
    if len(p) == 6:
        p[0] = IfStatement(condition=p[3], then_branch=p[5])
    else:
        p[0] = IfStatement(condition=p[3], then_branch=p[5], else_branch=p[7])

def p_return_stmt(p):
    """return_stmt : RETURN expression SEMICOLON"""
    p[0] = ReturnStatement(expression=p[2])

def p_expr_stmt(p):
    """expr_stmt : expression SEMICOLON"""
    p[0] = p[1]

def p_expression_binop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression ASSIGN expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression"""
    p[0] = BinaryOperation(left=p[1], operator=p[2], right=p[3])

def p_expression_uminus(p):
    """expression : MINUS expression %prec UMINUS"""
    p[0] = UnaryOperation(operator='-', operand=p[2])

def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_expression_number(p):
    """expression : INT_LITERAL
                  | FLOAT_LITERAL"""
    p[0] = Literal(value=p[1])

def p_expression_identifier(p):
    """expression : IDENTIFIER"""
    p[0] = Identifier(name=p[1])

def p_empty(p):
    """empty :"""
    p[0] = None

def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Function to parse tokens and build AST
def parse_tokens(tokens_list):
    # Convert tokens to a format suitable for PLY
    lexer = LexerFromTokens(tokens_list)
    return parser.parse(lexer=lexer)

class LexerFromTokens:
    """A mock lexer that feeds tokens from a list to the parser."""

    def __init__(self, tokens_list):
        self.tokens = tokens_list
        self.index = 0

    def token(self):
        if self.index < len(self.tokens):
            tok = self.tokens[self.index]
            self.index += 1
            return tok
        else:
            return None
