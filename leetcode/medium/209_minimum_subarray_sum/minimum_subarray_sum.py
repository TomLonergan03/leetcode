import sys
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum_length = sys.maxsize
        left = 0
        right = 1
        size = len(nums)
        while left != size:
            current_sum = sum(nums[left:right], 0)
            print(current_sum, "for", nums[left:right])
            if current_sum == target:
                minimum_length = min(minimum_length, right - left)
                left += 1
            elif current_sum < target:
                if right < size:
                    right += 1
                else:
                    break
            else:
                left += 1
        if minimum_length == sys.maxsize:
            return 0
        return minimum_length


# print(Solution().minSubArrayLen(7, [4, 3, 2, 2, 2, 7]))
print(Solution().minSubArrayLen(11, [1, 2, 3, 4, 5]))
