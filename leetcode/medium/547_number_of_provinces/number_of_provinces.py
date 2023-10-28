from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        regions = 0
        for i in range(len(isConnected)):
            if i not in self.visited:
                self.search(i, isConnected)
                regions += 1
        return regions

    def search(self, i, isConnected: List[List[int]]):
        to_visit = [i]
        while to_visit:
            next = to_visit.pop()
            self.visited.add(next)
            for j in range(len(isConnected)):
                if j != next and isConnected[next][j] and j not in self.visited:
                    to_visit.append(j)


print(Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
