# src/parser/ast_nodes.py

class ASTNode:
    """Base class for all AST nodes."""
    pass

class Program(ASTNode):
    def __init__(self, declarations):
        self.declarations = declarations

    def __repr__(self):
        return f"Program(declarations={self.declarations})"

class FunctionDeclaration(ASTNode):
    def __init__(self, return_type, name, params, body):
        self.return_type = return_type
        self.name = name
        self.params = params
        self.body = body

    def __repr__(self):
        return f"FunctionDeclaration(return_type={self.return_type}, name={self.name}, params={self.params}, body={self.body})"

class VariableDeclaration(ASTNode):
    def __init__(self, var_type, name, initializer=None):
        self.var_type = var_type
        self.name = name
        self.initializer = initializer

    def __repr__(self):
        return f"VariableDeclaration(var_type={self.var_type}, name={self.name}, initializer={self.initializer})"

class IfStatement(ASTNode):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

    def __repr__(self):
        return f"IfStatement(condition={self.condition}, then_branch={self.then_branch}, else_branch={self.else_branch})"

class ReturnStatement(ASTNode):
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"ReturnStatement(expression={self.expression})"

class BinaryOperation(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BinaryOperation(left={self.left}, operator='{self.operator}', right={self.right})"

class UnaryOperation(ASTNode):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def __repr__(self):
        return f"UnaryOperation(operator='{self.operator}', operand={self.operand})"

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Identifier(name='{self.name}')"

class Literal(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Literal(value={self.value})"

class CompoundStatement(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"CompoundStatement(statements={self.statements})"
