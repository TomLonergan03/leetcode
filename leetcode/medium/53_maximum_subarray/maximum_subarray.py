from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maximum_sum = -(10**5)
        current_sum = 0
        for num in nums:
            current_sum += num
            maximum_sum = max(maximum_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return maximum_sum


print(Solution().maxSubArray([-2, -1]))
print(Solution().maxSubArray([2, -3, 1, 3, -3, 2, 2, 1]))
