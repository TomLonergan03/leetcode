from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]].append(i)
            else:
                nums_dict[nums[i]] = [i]
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in nums_dict:
                if needed == nums[i]:
                    if len(nums_dict[needed]) <= 1:
                        continue
                    return [nums_dict[needed][0], nums_dict[needed][1]]
                return [i, nums_dict[needed][0]]


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))
