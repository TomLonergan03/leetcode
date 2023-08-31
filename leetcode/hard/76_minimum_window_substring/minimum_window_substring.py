class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if m < n:
            return ""
        counts = {}
        for char in t:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        t = counts

        left = 0
        right = 1

        minimum_length = m
        start = 0
        solution = False
        substring_count = {s[0]: 1}
        while left < m:
            if self.compareCounts(t, substring_count):
                solution = True
                length = right - left
                if length < minimum_length:
                    minimum_length = length
                    start = left
                if substring_count[s[left]] == 1:
                    substring_count.pop(s[left])
                else:
                    substring_count[s[left]] -= 1
                left += 1
            elif right == m:
                if substring_count[s[left]] == 1:
                    substring_count.pop(s[left])
                else:
                    substring_count[s[left]] -= 1
                left += 1
            elif right != m:
                if s[right] in substring_count:
                    substring_count[s[right]] += 1
                else:
                    substring_count[s[right]] = 1
                right += 1
            if right == m:
                if right - left < n:
                    break
        if not solution:
            return ""
        return s[start:start + minimum_length]

    def compareCounts(self, t, substring) -> bool:
        for key in t.keys():
            if key not in substring:
                return False
            if t[key] > substring[key]:
                return False
        return True


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("ab", "b"))
