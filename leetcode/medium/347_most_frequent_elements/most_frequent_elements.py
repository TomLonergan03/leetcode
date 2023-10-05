from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        counts = sorted(list(counts.items()), key=lambda x: -x[1])
        return list(map(lambda x: x[0], counts[:k]))
