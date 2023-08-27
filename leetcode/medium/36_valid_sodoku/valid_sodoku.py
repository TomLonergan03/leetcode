class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if not self.checkArray(row):
                return False
        board = sum(board, [])
        for i in range(9):
            if not self.checkCol(i, board):
                return False
        for i in [0, 3, 6, 27, 30, 33, 54, 57, 60]:
            if not self.checkSquare(i, board):
                return False
        return True

    def checkArray(self, row):
        return 10 - row.count(".") - len(set(row)) == 0

    def checkCol(self, col_number, board):
        col = board[col_number::9]
        return self.checkArray(col)

    def checkSquare(self, top_right, board):
        square = board[top_right:top_right + 3] + \
            board[top_right + 9:top_right + 12] + \
            board[top_right + 18:top_right + 21]
        return self.checkArray(square)
