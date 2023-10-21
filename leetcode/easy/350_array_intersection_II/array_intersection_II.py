from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1count = Counter(nums1)
        nums2count = Counter(nums2)
        result = []
        for key in nums1count.keys():
            if key in nums1count and key in nums2count:
                result.extend([key] * min(nums1count[key], nums2count[key]))
        return result
