class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)

        result = ""

        num1 = "".join(list(reversed(num1)))
        num2 = "".join(list(reversed(num2)))

        carry = 0
        for i in range(min(m, n)):
            sum, carry = self.addChar(num1[i], num2[i], carry)
            result += sum

        if m < n:
            for i in range(m, n):
                sum, carry = self.addChar(num2[i], "0", carry)
                result += sum
        elif n < m:
            for i in range(n, m):
                sum, carry = self.addChar(num1[i], "0", carry)
                result += sum
        if carry == 1:
            result += "1"
        return "".join(list(reversed(result)))

    def addChar(self, char1: str, char2: str, carry: int):
        sum = int(char1) + int(char2) + carry
        if sum > 9:
            sum %= 10
            carry = 1
        else:
            carry = 0
        return (str(sum), carry)
