from dataclasses import dataclass
from typing import Union

@dataclass
class Instruction:
    operation: str
    operand: Union[int, str, None] = None
