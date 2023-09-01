from typing import List
import sys


class Solution:
    def jump(self, nums: List[int]) -> int:
        min_to_here = [sys.maxsize for _ in range(len(nums))]
        min_to_here[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    break
                min_to_here[i + j] = min(min_to_here[i + j],
                                         min_to_here[i] + 1)
        return min_to_here[-1]


print(Solution().jump([2, 3, 1, 1, 4]))
