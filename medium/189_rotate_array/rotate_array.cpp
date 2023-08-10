#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
  static void rotate(std::vector<int> &nums, int k) {
    int n = nums.size();
    k = k % n;
    std::reverse(nums.begin(), nums.begin() + (n - k));
    std::reverse(nums.begin() + (n - k), nums.end());
    std::reverse(nums.begin(), nums.end());
  }
};

int main(int argc, char const *argv[]) {
  std::vector<int> nums{1, 2, 3, 4, 5, 6, 7};
  Solution::rotate(nums, 3);
  for (int i : nums) {
    std::cout << i << ' ';
  }
  std::cout << '\n';
  return 0;
}
