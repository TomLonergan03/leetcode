from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack[0]


print(Solution().evalRPN(["10", "6", "9", "3", "+",
      "-11", "*", "/", "*", "17", "+", "5", "+"]))
