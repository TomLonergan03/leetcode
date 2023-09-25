from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        arrows = 1
        n = len(points)
        temp = points[0][1]
        for i in range(n):
            if temp < points[i][0]:
                arrows += 1
                temp = points[i][1]
        return arrows


print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
