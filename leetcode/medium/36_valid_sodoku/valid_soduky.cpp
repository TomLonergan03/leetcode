#include <array>
#include <cstdio>
#include <cstdlib>
#include <vector>

class Solution {
public:
  bool isValidSudoku(std::vector<std::vector<char>> &board) {
    for (int i = 0; i < 9; i++) {
      const auto row = board[i];
      std::vector<char> col;
      for (int j = 0; j < 9; j++) {
        col.push_back(board[j][i]);
      }
      std::vector<char> box;
      for (int j = 0; j < 9; j++) {
        const int box_x = i % 3;
        const int box_y = i / 3;
        const int x = box_x * 3 + j % 3;
        const int y = box_y * 3 + j / 3;
        box.push_back(board[x][y]);
      }
      if (!(isValid(row) && isValid(col) && isValid(box))) {
        return false;
      }
    }
    return true;
  }

private:
  bool isValid(const std::vector<char> &row) {
    std::array<bool, 9> seen{false};
    for (const auto cell : row) {
      if (cell == '.') {
        continue;
      }
      const auto val = cell - '0';
      if (seen[val - 1]) {
        return false;
      };
      seen[val - 1] = true;
    }
    return true;
  }
};
