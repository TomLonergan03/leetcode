from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        value = [None] * length
        value[0] = nums[0]
        value[1] = nums[1]
        if length == 2:
            return max(value)
        value[2] = nums[2] + nums[0]
        if length == 3:
            return max(value)
        for i in range(3, length):
            value[i] = nums[i] + max(value[i - 2], value[i - 3])
        return max(value[-1], value[-2])


print(Solution().rob([2, 7, 9, 3, 1]))
print(Solution().rob([0, 0]))
