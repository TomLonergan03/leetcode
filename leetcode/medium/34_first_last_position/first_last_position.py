from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)
        if right == 0:
            return [-1, -1]
        index = self.binarySearch(nums, target, left, right)
        if index == -1:
            return [-1, -1]
        left_end = index
        for i in range(index - 1, -1, -1):
            if nums[i] == target:
                left_end = i
            else:
                break
        right_end = index
        for i in range(index, right):
            if nums[i] == target:
                right_end = i
            else:
                break
        return [left_end, right_end]

    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        if nums[left] == target:
            return left
        if right - left == 1:
            return -1
        mid = left + (right - left) // 2
        if target < nums[mid]:
            return self.binarySearch(nums, target, left, mid)
        elif target == nums[mid]:
            return mid
        else:
            return self.binarySearch(nums, target, mid, right)


print(Solution().searchRange([1, 2, 2, 2, 3, 4], 2))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
print(Solution().searchRange([], 0))
print(Solution().searchRange([0, 0, 1, 2, 2], 2))
