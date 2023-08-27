class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t == "":
            return True
        s_size = len(s)
        s_index = 0
        for char in t:
            if s_index >= s_size:
                return True
            if char == s[s_index]:
                s_index += 1
        if s_index >= s_size:
            return True
        return False
