class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars = []
        while columnNumber > 0:
            columnNumber -= 1
            chars.append(chr(columnNumber % 26 + ord("A")))
            columnNumber //= 26
        chars.reverse()
        return "".join(chars)


print(Solution().convertToTitle(1))
print(Solution().convertToTitle(28))
print(Solution().convertToTitle(701))
