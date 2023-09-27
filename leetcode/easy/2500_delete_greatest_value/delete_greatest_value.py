from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        total = 0
        grid = [sorted(row) for row in grid]
        for i in range(len(grid[0])):
            possible = []
            for j in range(len(grid)):
                possible.append(grid[j][i])
            total += max(possible)
        return total


print(Solution().deleteGreatestValue([[1, 2, 4], [3, 3, 1]]))
print(Solution().deleteGreatestValue([[10]]))
print(Solution().deleteGreatestValue([[9, 81], [33, 17]]))
