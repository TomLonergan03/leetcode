from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longest = 0
        current = 0
        for key in values:
            if key - 1 in values:
                continue
            current = 0
            while key in values:
                key += 1
                current += 1
            longest = max(longest, current)
        return longest
