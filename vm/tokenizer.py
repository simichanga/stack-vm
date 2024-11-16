from typing import List

def tokenize(expression: str) -> List[str]:
    tokens = []
    num = ""
    identifier = ""

    for char in expression:
        if char.isdigit():
            num += char  # build multi-digit numbers
        elif char.isalpha():  # build identifiers
            identifier += char
        else:
            if num:
                tokens.append(num)
                num = ""
            if identifier:
                tokens.append(identifier)
                identifier = ""
            if char in "+-*/=()":
                tokens.append(char)
    if num:
        tokens.append(num)
    if identifier:
        tokens.append(identifier)
    return tokens
