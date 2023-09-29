from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        state = "undecided"
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if state == "undecided":
                    state = "increasing"
                elif state == "decreasing":
                    return False
            elif nums[i] < nums[i - 1]:
                if state == "undecided":
                    state = "decreasing"
                elif state == "increasing":
                    return False
        return True
