from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        left = 0
        right = 0
        queue = deque()
        while right < len(nums):
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()
            queue.append(right)

            if left > queue[0]:
                queue.popleft()

            if right + 1 >= k:
                maxes.append(nums[queue[0]])
                left += 1

            right += 1

        return maxes


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(Solution().maxSlidingWindow([1], 1))
