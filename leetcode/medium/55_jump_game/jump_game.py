from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        if 0 in nums:
            zero_locs = [i for i, x in enumerate(nums) if x == 0]
            for zero in zero_locs:
                result = self.canSkip(nums, zero)
                if not result:
                    return False
        return True

    def canSkip(self,  nums: List[int], index: int) -> bool:
        for position in reversed(range(0, index)):
            if nums[position] + position > index or nums[position] + position >= len(nums) - 1:
                return True
        return False


if __name__ == "__main__":
    print("[2, 3, 1, 1, 4]", Solution().canJump([2, 3, 1, 1, 4]))
    print("[3, 2, 1, 0, 4]", Solution().canJump([3, 2, 1, 0, 4]))
    print("[0]", Solution().canJump([0]))
    print("[2, 0, 0]", Solution().canJump([2, 0, 0]))
