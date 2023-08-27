class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        max_width = 0
        while left <= len(s):
            max_width = max(max_width, right - left - 1)
            if len(set(s[left:right])) < right-left:
                left += 1
            else:
                right += 1
        return max_width
