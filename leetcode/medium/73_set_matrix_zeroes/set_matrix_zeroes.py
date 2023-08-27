from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeroes = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroes.append((i, j))

        for (x, y) in zeroes:
            for i in range(n):
                matrix[x][i] = 0
            for i in range(m):
                matrix[i][y] = 0


if __name__ == "__main__":
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol = Solution()
    sol.setZeroes(matrix)
    print(matrix)
