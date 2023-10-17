from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = 10**5
        min_index = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                current_distance = abs(
                    points[i][0] - x) + abs(points[i][1] - y)
                if current_distance < min_distance:
                    min_distance = current_distance
                    min_index = i
        return min_index
