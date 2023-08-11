#include <iostream>
#include <vector>

class Solution {
public:
  int maxProfit(std::vector<int> &prices) {
    int max = prices[0];
    int min = prices[0];
    int max_profit = 0;
    for (int i : prices) {
      if (i < min) {
        min = i;
      }
      if ((i - min) > max_profit) {
        max = i;
        max_profit = max - min;
      }
    }
    return max_profit;
  }
};

int main(int argc, char const *argv[]) {
  Solution sol = Solution();
  std::vector<int> vec{2, 4, 1};
  std::cout << sol.maxProfit(vec) << std::endl;
  return 0;
}
