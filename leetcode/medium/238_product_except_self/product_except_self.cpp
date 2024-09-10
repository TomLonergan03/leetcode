#include <vector>

class Solution {
public:
  std::vector<int> productExceptSelf(std::vector<int> &nums) {
    std::vector<int> result(nums.size(), 1);
    int left = 1;
    int right = 1;
    for (int i = 0; i < nums.size(); i++) {
      result[i] *= left;
      result[nums.size() - 1 - i] *= right;
      left *= nums[i];
      right *= nums[nums.size() - 1 - i];
    }
    return result;
  }
};
