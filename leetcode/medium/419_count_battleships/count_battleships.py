from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n = len(board)
        m = len(board[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == ".":
                    continue
                if i == 0 and j == 0:
                    count += 1
                elif i == 0 and board[i][j - 1] == ".":
                    count += 1
                elif j == 0 and board[i - 1][j] == ".":
                    count += 1
                elif board[i][j - 1] == "." and board[i - 1][j] == ".":
                    count += 1
        return count
