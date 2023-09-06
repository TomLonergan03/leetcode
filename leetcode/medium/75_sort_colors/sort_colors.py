from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        mid = 0
        two = len(nums) - 1
        while mid <= two:
            if nums[mid] == 0:
                nums[mid], nums[zero] = nums[zero], nums[mid]
                zero += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[two] = nums[two], nums[mid]
                two -= 1
            else:
                mid += 1
