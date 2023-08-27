from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        citations.append(0)
        for i in range(len(citations)):
            if citations[i] <= i:
                return i


print(Solution().hIndex([3, 0, 6, 1, 5]))
print(Solution().hIndex([1]))
