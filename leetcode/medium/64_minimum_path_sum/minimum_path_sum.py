from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        minimum_path = [[None for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    minimum_path[i][j] = grid[i][j]
                elif i == 0:
                    minimum_path[i][j] = minimum_path[i][j - 1] + grid[i][j]
                elif j == 0:
                    minimum_path[i][j] = minimum_path[i - 1][j] + grid[i][j]
                else:
                    minimum_path[i][j] = min(
                        minimum_path[i - 1][j], minimum_path[i][j - 1]) + grid[i][j]
        return minimum_path[-1][-1]


print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(Solution().minPathSum([[1, 2, 3], [4, 5, 6]]))
