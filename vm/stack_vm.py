from typing import List, Dict, Callable, Union
from .instruction import Instruction

class StackVM:
    def __init__(self):
        self.stack: List[int] = []
        self.instructions: List[Instruction] = []
        self.memory: Dict[str, int] = {}  # memory to store variables
        self.operations: Dict[str, Callable[[Union[int, None, str]], None]] = {
            "PUSH": self.push,
            "POP": self.pop,
            "ADD": lambda _: self.binary_op(lambda a, b: a + b, "ADD"),
            "SUB": lambda _: self.binary_op(lambda a, b: a - b, "SUB"),
            "MUL": lambda _: self.binary_op(lambda a, b: a * b, "MUL"),
            "DIV": lambda _: self.binary_op(lambda a, b: a // b if b != 0 else self.raise_div_zero(), "DIV"),
            "PRINT": lambda _: self.print_top(),
            "STORE": self.store,
            "LOAD": self.load,
        }
    
    def load_instructions(self, instructions: List[Instruction]):
        self.instructions = instructions
    
    def run(self):
        for instruction in self.instructions:
            operation = self.operations.get(instruction.operation)
            if operation:
                operation(instruction.operand)
            else:
                raise ValueError(f"Unknown operation: {instruction.operation}")

    # Stack operations
    def push(self, value: int):
        self.stack.append(value)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        raise IndexError("POP from an empty stack")
    
    def binary_op(self, func: Callable[[int, int], int], op_name: str):
        b, a = self.pop(), self.pop()
        result = func(a, b)
        self.push(result)

    def raise_div_zero(self):
        raise ZeroDivisionError("Division by zero")
    
    def print_top(self):
        if self.stack:
            print(self.stack[-1])
        else:
            print("Stack is empty.")

    # Variable handling
    def store(self, var_name: str):
        value = self.pop()
        self.memory[var_name] = value

    def load(self, var_name: str):
        if var_name in self.memory:
            self.push(self.memory[var_name])
        else:
            raise ValueError(f"Undefined variable: {var_name}")
