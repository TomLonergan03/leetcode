#include <algorithm>
#include <stack>
#include <utility>
#include <vector>

class Solution {
public:
  int largestRectangleArea(std::vector<int> &heights) {
    std::stack<std::pair<int, int>> stack;
    int current_highest = 0;
    int max_area = 0;
    for (int i = 0; i < heights.size(); i++) {
      int start = i;
      while (stack.size() && stack.top().second > heights[i]) {
        const auto top = stack.top();
        max_area = std::max(max_area, top.second * (i - top.first));
        start = top.first;
        stack.pop();
      }
      stack.push({start, heights[i]});
    }
    while (stack.size()) {
      const auto top = stack.top();
      max_area = std::max(
          max_area, top.second * static_cast<int>(heights.size() - top.first));
      stack.pop();
    }
    return max_area;
  }
};
