class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        current = 0
        sign = 1
        stack = []
        for char in s:
            if char.isnumeric():
                current = current * 10 + int(char)
            elif char == "+":
                result += sign * current
                current = 0
                sign = 1
            elif char == "-":
                result += sign * current
                current = 0
                sign = -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif char == ")":
                result += sign * current
                current = 0
                result *= stack.pop()
                result += stack.pop()
        if current:
            result += sign * current
        return result
