class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        factor = 1
        if x[0] == "-":
            factor = -1
            x = x[1:]
        x = factor * int("".join(list(reversed(x))))
        if x < pow(-2, 31) or x > pow(2, 31) - 1:
            return 0
        return x
