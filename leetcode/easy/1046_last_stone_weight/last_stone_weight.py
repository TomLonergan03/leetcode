from typing import List
from heapq import heappop, heappush, heapify


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapify(stones)
        while len(stones) > 1:
            y = -heappop(stones)
            x = -heappop(stones)
            if x == y:
                continue
            heappush(stones, -(y - x))
        if not stones:
            return 0
        return -stones[0]


Solution().lastStoneWeight([2, 7, 4, 1, 8, 1])
