from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        best_including = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    best_including[i] = max(best_including[i], best_including[j] + 1)
        return max(best_including)


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
