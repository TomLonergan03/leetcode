from typing import List
from heapq import heapify, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: - 1 * x, nums))
        heapify(nums)
        print(nums)
        for _ in range(k - 1):
            heappop(nums)
        return -heappop(nums)


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
