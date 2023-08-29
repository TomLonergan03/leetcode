class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1) + 1
        len2 = len(word2) + 1
        if len1 == 0:
            return len2
        if len2 == 0:
            return len1
        edits = [[None for _ in range(len1)] for _ in range(len2)]
        for i in range(len2):
            for j in range(len1):
                if i == 0:
                    edits[i][j] = j
                elif j == 0:
                    edits[i][j] = i
                elif word1[j - 1] == word2[i - 1]:
                    edits[i][j] = edits[i - 1][j - 1]
                else:
                    edits[i][j] = min(
                        edits[i][j - 1], edits[i - 1][j], edits[i - 1][j - 1]) + 1
        return edits[-1][-1]


print(Solution().minDistance("horse", "ros"))
print(Solution().minDistance("a", "a"))
print(Solution().minDistance("a", "ab"))
print(Solution().minDistance("zoologicoarchaeologist", "zoogeologist"))
print(Solution().minDistance(
    "pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically"))
