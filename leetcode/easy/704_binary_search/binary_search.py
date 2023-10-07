from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.rec(nums, target, 0, len(nums))

    def rec(self, nums, target, left, right):
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if right - left <= 1:
            return -1
        if nums[mid] < target:
            return self.rec(nums, target, mid, right)
        if nums[mid] > target:
            return self.rec(nums, target, left, mid)


Solution().search([-1, 0, 3, 5, 9, 12], 9)
