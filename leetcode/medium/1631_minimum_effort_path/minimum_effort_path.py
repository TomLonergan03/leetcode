from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        cols = len(heights[0])
        rows = len(heights)
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        efforts = [[inf for _ in range(cols)] for _ in range(rows)]
        efforts[0][0] = 0
        next_nodes = [(0, 0, 0)]
        while next_nodes:
            effort, x, y = heappop(next_nodes)
            if x == rows - 1 and y == cols - 1:
                return effort

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    new_effort = max(effort, abs(
                        heights[x][y] - heights[nx][ny]))
                    if new_effort < efforts[nx][ny]:
                        efforts[nx][ny] = new_effort
                        heappush(next_nodes, (new_effort, nx, ny))
        return efforts[-1][-1]


print(Solution().minimumEffortPath(
    [[1, 2, 1, 1, 1],
     [1, 2, 1, 2, 1],
     [1, 2, 1, 2, 1],
     [1, 2, 1, 2, 1],
     [1, 1, 1, 2, 1]]))
