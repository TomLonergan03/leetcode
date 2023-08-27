from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        triangle_size = len(triangle)
        minimum_path = [[None for _ in range(
            triangle_size)] for _ in range(triangle_size)]
        minimum_path[0][0] = triangle[0][0]
        for i in range(1, triangle_size):
            for j in range(len(triangle[i])):
                if j == 0:
                    minimum_path[i][j] = minimum_path[i - 1][j] + \
                        triangle[i][j]
                elif minimum_path[i - 1][j] == None:
                    minimum_path[i][j] = minimum_path[i -
                                                      1][j - 1] + triangle[i][j]
                else:
                    minimum_path[i][j] = min(
                        minimum_path[i - 1][j], minimum_path[i - 1][j - 1]) + triangle[i][j]
        return min(minimum_path[-1])


print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
