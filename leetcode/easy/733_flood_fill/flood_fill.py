from typing import List
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        queue.appendleft((sr, sc))
        start_color = image[sr][sc]
        while queue:
            x, y = queue.pop()
            if image[x][y] != start_color or image[x][y] == color:
                continue
            image[x][y] = color
            if x > 0:
                queue.appendleft((x - 1, y))
            if x < len(image) - 1:
                queue.appendleft((x + 1, y))
            if y > 0:
                queue.appendleft((x, y - 1))
            if y < len(image[0]) - 1:
                queue.appendleft((x, y + 1))
        return image


print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
