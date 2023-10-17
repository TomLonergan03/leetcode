class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        s1_missing = ""
        s2_missing = ""
        for i in range(len(s1)):
            if count > 2:
                return False
            if s1[i] != s2[i]:
                count += 1
                s1_missing += s1[i]
                s2_missing += s2[i]
        if count != 0 and count != 2:
            return False
        if set([char for char in s1_missing]) != set([char for char in s2_missing]):
            return False
        return True


Solution().areAlmostEqual("tozo", "ootz")
