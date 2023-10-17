from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edges[0].extend(edges[1])
        for element in set(edges[0]):
            if edges[0].count(element) > 1:
                return element


Solution().findCenter([[1, 2], [2, 3], [4, 2]])
