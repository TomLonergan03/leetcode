from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = dict(zip(nums, [0] * len(nums)))
        target = len(nums) / 2
        for element in nums:
            counts[element] += 1
            if counts[element] > target:
                return element
