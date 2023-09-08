from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        result = []
        for i in matrix:
            result.extend(i)
        matrix = result
        left = 0
        right = len(matrix)
        return self.recurse(matrix, left, right, target)

    def recurse(self, flat_matrix: List[int], left: int, right: int, target: int):
        if right - left == 1:
            if flat_matrix[left] == target:
                return True
            return False
        mid = left + (right - left) // 2
        if flat_matrix[mid] == target:
            return True
        elif flat_matrix[mid] > target:
            return self.recurse(flat_matrix, left, mid, target)
        else:
            return self.recurse(flat_matrix, mid, right, target)


print(Solution().searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
