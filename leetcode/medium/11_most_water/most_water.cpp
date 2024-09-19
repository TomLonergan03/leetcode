#include <cstdint>
#include <vector>

class Solution {
public:
  int maxArea(std::vector<int> &height) {
    size_t left = 0;
    size_t right = height.size() - 1;
    std::uint32_t max = 0;
    for (int _ = 0; _ < height.size() - 1; _++) {
      const std::uint32_t current =
          std::min(height[left], height[right]) * (right - left);
      max = std::max(max, current);
      if (height[left] < height[right]) {
        left++;
      } else {
        right--;
      }
    };
    return max;
  }
};
