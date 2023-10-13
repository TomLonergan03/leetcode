from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums1 = set(nums1)
        nums2 = set(nums2)
        for item in nums1:
            if item in nums2:
                result.add(item)
        return list(result)
