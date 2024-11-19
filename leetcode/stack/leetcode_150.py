"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = "-+*/"
        for i in tokens:
            if i in operands:
                if i == "+":
                    stack.append(stack.pop() + stack.pop())
                if i == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                if i == "*":
                    stack.append(stack.pop() * stack.pop())
                if i == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b // a)
            else:
                stack.append(int(i))
        return stack[0]


case1 = ["2", "1", "+", "3", "*"]
case2 = ["4", "13", "5", "/", "+"]

s = Solution()

print(s.evalRPN(case1))
print(s.evalRPN(case2))
