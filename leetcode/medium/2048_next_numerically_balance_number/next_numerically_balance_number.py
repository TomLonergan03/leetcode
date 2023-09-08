from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        i = n + 1
        while True:
            if self.isBalanced(i):
                return i
            i += 1

    def isBalanced(self, n):
        counts = Counter(str(n))
        for char in str(n):
            if int(counts[char]) != int(char):
                return False
        return True
