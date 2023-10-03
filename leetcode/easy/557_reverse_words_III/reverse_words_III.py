class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(map(lambda x: "".join(reversed(x)), s.split())))


print(Solution().reverseWords("abc def"))
