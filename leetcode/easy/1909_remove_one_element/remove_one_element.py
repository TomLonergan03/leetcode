from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                if i == len(nums) - 1:
                    nums.pop(i)
                elif nums[i - 1] > nums[i + 1] or i == 1:
                    nums.pop(i - 1)
                else:
                    nums.pop(i)
                break
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False
        return True


print(Solution().canBeIncreasing([105, 924, 32, 968]))
print(Solution().canBeIncreasing([1, 1]))
print(Solution().canBeIncreasing([100, 21, 100]))
