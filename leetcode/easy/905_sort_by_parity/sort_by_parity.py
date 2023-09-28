from collections import deque
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sorted = deque()
        for num in nums:
            if num % 2 == 0:
                sorted.appendleft(num)
            else:
                sorted.append(num)
        return list(sorted)