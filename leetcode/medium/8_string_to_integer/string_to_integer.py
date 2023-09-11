class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) < 1:
            return 0
        if s[0] == "-":
            factor = -1
        else:
            factor = 1
        if s[0] == "-" or s[0] == "+":
            s = s[1:]
        result = 0
        for char in s:
            char_ascii = ord(char)
            if char_ascii < 48 or char_ascii > 57:
                break
            result *= 10
            result += char_ascii - 48
        result *= factor
        if result > 2**31 - 1:
            result = 2**31 - 1
        elif result < -(2**31):
            result = -(2**31)
        return result
