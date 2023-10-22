from math import isqrt
from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = list(map(lambda x: -x, gifts))
        heapify(gifts)
        for i in range(k):
            pile = -heappop(gifts)
            pile = isqrt(pile)
            heappush(gifts, -pile)
        return -sum(gifts)


print(Solution().pickGifts([25, 64, 8, 4, 100], 4))
