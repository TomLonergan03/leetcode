class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = [["" for _ in range(len(s))] for _ in range(numRows)]
        row = 0
        col = 0
        diagonaling = False
        for char in s:
            zigzag[row][col] = char
            if row == 0:
                diagonaling = False
            if row == numRows - 1:
                diagonaling = True
            if diagonaling:
                row -= 1
                col += 1
            else:
                row += 1
        result = ''
        for row in zigzag:
            for char in row:
                result += char
        return result


print(Solution().convert("PAYPALISHIRING", 3))
print("PAHNAPLSIIGYIR")
