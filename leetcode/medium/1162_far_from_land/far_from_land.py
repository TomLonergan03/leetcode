from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        to_visit = deque()
        visited = set()
        n = len(grid)
        m = len(grid[0])
        distance = [[None for _ in range(m)] for _ in range(n)]
        islands = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 1:
                    to_visit.append((x, y, 0))
                    visited.add((x, y))
        if not visited or len(visited) == n * m:
            return -1
        while to_visit:
            x, y, dist = to_visit.popleft()
            distance[x][y] = dist
            if x > 0 and (x - 1, y) not in visited:
                to_visit.append((x - 1, y, dist + 1))
                visited.add((x - 1, y))
            if x < n - 1 and (x + 1, y) not in visited:
                to_visit.append((x + 1, y, dist + 1))
                visited.add((x + 1, y))
            if y > 0 and (x, y - 1) not in visited:
                to_visit.append((x, y - 1, dist + 1))
                visited.add((x, y - 1))
            if y < m - 1 and (x, y + 1) not in visited:
                to_visit.append((x, y + 1, dist + 1))
                visited.add((x, y + 1))
            if len(to_visit) == 1:
                return to_visit.pop()[2]


# print(Solution().maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
# print(Solution().maxDistance(
#     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
print(Solution().maxDistance(
    [[1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 0, 1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 1, 1, 1, 1, 1, 0, 0]]))
