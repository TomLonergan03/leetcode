class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        alternate = min(m, n)
        result = ""
        for i in range(alternate):
            result += word1[i] + word2[i]
        if m < n:
            result += word2[alternate:]
        if n < m:
            result += word1[alternate:]
        return result
