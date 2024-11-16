from vm.stack_vm import StackVM
from vm.tokenizer import tokenize
from vm.parser import handle_assignment

# Initialize a single instance of StackVM to maintain state
vm = StackVM()

def evaluate_expression(expression: str):
    tokens = tokenize(expression)
    instructions = handle_assignment(tokens)
    
    vm.load_instructions(instructions)
    vm.run()

# Example usage
if __name__ == "__main__":
    # Variable assignment example
    evaluate_expression("x = 10")       # Sets x to 10
    evaluate_expression("y = x + 5")    # Sets y to 15
    evaluate_expression("y * 2")        # Prints 30
