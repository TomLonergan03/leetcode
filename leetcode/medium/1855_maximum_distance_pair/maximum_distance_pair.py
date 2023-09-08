from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        max_distance = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                max_distance = max(max_distance, j - i)
                j += 1
        return max_distance


print(Solution().maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]))
print(Solution().maxDistance([5, 4], [3, 2]))
