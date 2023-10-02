from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(len(nums)):
            if i not in nums:
                return i
        return 0


print(Solution().missingNumber([3, 0, 1]))
