from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        paths_to = [[0 for _ in range(len(obstacleGrid[0]))]
                    for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == 0 and j == 0:
                    paths_to[i][j] = 1
                elif i == 0:
                    paths_to[i][j] = paths_to[i][j - 1]
                elif j == 0:
                    paths_to[i][j] = paths_to[i - 1][j]
                else:
                    paths_to[i][j] = paths_to[i - 1][j] + paths_to[i][j - 1]
        return paths_to[-1][-1]


print(Solution().uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]]))
