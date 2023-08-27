class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        starts = []
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                starts.append(i)
        for start in starts:
            j = 0
            for i in range(start, len(haystack)):
                if haystack[i] != needle[j]:
                    break
                j += 1
                if j == len(needle):
                    return start
        return -1


print(Solution().strStr("a", "a"))
