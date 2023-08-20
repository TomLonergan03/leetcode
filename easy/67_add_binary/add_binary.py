class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(x) for _, x in enumerate(a)]
        b = [int(x) for _, x in enumerate(b)]
        a = a[::-1]
        b = b[::-1]
        result = []
        carry = 0
        len_a = len(a)
        len_b = len(b)
        for i in range(max(len_a, len_b)):
            if i >= len_a:
                carry, digit = self.addDigit(0, b[i], carry)
            elif i >= len_b:
                carry, digit = self.addDigit(a[i], 0, carry)
            else:
                carry, digit = self.addDigit(a[i], b[i], carry)
            result.append(str(digit))
        if carry == 1:
            result.append("1")
        return ''.join(result[::-1])

    def addDigit(self, a: int, b: int, carry: int) -> (int, int):
        sum = a + b + carry
        match sum:
            case 3:
                return (1, 1)
            case 2:
                return (1, 0)
            case 1:
                return (0, 1)
            case 0:
                return (0, 0)


print(Solution().addBinary("1010", "1011"))
print(Solution().addBinary("11", "1"))
print(Solution().addBinary("0", "0"))
print(Solution().addBinary("1", "111"))
