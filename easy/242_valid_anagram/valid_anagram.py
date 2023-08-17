class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counts = {}
        for char in s:
            if not char in s_counts:
                s_counts[char] = 1
            else:
                s_counts[char] += 1
        for char in t:
            if not char in s_counts:
                return False
            s_counts[char] -= 1
            if s_counts[char] < 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isAnagram("anagram", "nagaram"))
