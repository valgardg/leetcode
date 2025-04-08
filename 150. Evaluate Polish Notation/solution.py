from typing import List
import math
import re
patternInteger = re.compile("^[+-]?[0-9]+$")

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # print(f"stack: {stack}")
            if patternInteger.match(token):
                stack.append(token)
            else:
                el1 = stack.pop()
                el2 = stack.pop()
                expression = f"{el2}{token}{el1}"
                # print(f"Expression: {expression}")
                result = int(eval(expression))
                stack.append(result)

        return int(stack[0])