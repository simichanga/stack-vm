from typing import List
from .instruction import Instruction

def infix_to_postfix(tokens: List[str]) -> List[str]:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = []

    for token in tokens:
        if token.isdigit() or token.isidentifier():  # treat variables as identifiers
            output.append(token)
        elif token in precedence:
            while operators and operators[-1] != '(' and precedence[operators[-1]] >= precedence[token]:
                output.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()

    while operators:
        output.append(operators.pop())

    return output

def generate_instructions(postfix_tokens: List[str]) -> List[Instruction]:
    instructions = []
    for token in postfix_tokens:
        if token.isdigit():
            instructions.append(Instruction("PUSH", int(token)))
        elif token.isidentifier():  # Handle variable loading
            instructions.append(Instruction("LOAD", token))
        elif token == '+':
            instructions.append(Instruction("ADD"))
        elif token == '-':
            instructions.append(Instruction("SUB"))
        elif token == '*':
            instructions.append(Instruction("MUL"))
        elif token == '/':
            instructions.append(Instruction("DIV"))
    return instructions

def handle_assignment(tokens: List[str]) -> List[Instruction]:
    """Parses an assignment expression like `x = 10 + 5` or standalone expressions."""
    if '=' in tokens:
        var_name = tokens[0]  # left-hand side variable
        expression = tokens[2:]  # right-hand side expression
        postfix_tokens = infix_to_postfix(expression)
        instructions = generate_instructions(postfix_tokens)
        instructions.append(Instruction("STORE", var_name))
    else:
        postfix_tokens = infix_to_postfix(tokens)
        instructions = generate_instructions(postfix_tokens)
        instructions.append(Instruction("PRINT"))  # Ensure standalone expressions print the result
    return instructions
