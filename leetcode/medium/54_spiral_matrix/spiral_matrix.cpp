#include <iostream>
#include <vector>

enum Direction { kRight, kDown, kLeft, kUp };

class Solution {
public:
  std::vector<int> spiralOrder(std::vector<std::vector<int>> &matrix) {
    int x_start = -1;
    int y_start = 0;
    int x_end = matrix[0].size();
    int y_end = matrix.size();
    int x_location = 0;
    int y_location = 0;
    Direction direction = Direction::kRight;
    std::vector<int> spiralised;
    while (true) {
      if (spiralised.size() == (matrix[0].size() * matrix.size())) {
        break;
      }
      switch (direction) {
      case Direction::kRight:
        if (x_location < x_end) {
          spiralised.push_back(matrix[y_location][x_location]);
          x_location++;
        } else {
          y_location++;
          x_location--;
          x_end--;
          direction = Direction::kDown;
        }
        break;
      case Direction::kDown:
        if (y_location < y_end) {
          spiralised.push_back(matrix[y_location][x_location]);
          y_location++;
        } else {
          y_location--;
          x_location--;
          y_end--;
          direction = Direction::kLeft;
        }
        break;
      case Direction::kLeft:
        if (x_location > x_start) {
          spiralised.push_back(matrix[y_location][x_location]);
          x_location--;
        } else {
          x_location++;
          y_location--;
          x_start++;
          direction = Direction::kUp;
        }
        break;
      case Direction::kUp:
        if (y_location > y_start) {
          spiralised.push_back(matrix[y_location][x_location]);
          y_location--;
        } else {
          y_location++;
          x_location++;
          y_start++;
          direction = Direction::kRight;
        }
        break;
      }
    }
    return spiralised;
  }
};

int main(int argc, char const *argv[]) {
  std::vector<std::vector<int>> matrix{
      {1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
  auto result = Solution().spiralOrder(matrix);
  for (int element : result) {
    std::cout << element << " ";
  }
  std::cout << std::endl;
  return 0;
}
