class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        stack = []
        for word in words:
            stack.append(word)
        result = ""
        while stack:
            result += " " + stack.pop()
        return result[1:]
