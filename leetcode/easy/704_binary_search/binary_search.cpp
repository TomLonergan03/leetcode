#include <vector>

class Solution {
public:
  int search(std::vector<int> &nums, int target) {
    int left = 0, right = nums.size() - 1;
    while (true) {
      if (nums[left] == target) {
        return left;
      }
      if (nums[right] == target) {
        return right;
      }
      if (left >= right - 1) {
        return -1;
      }
      const int mid = left + (right - left) / 2;
      if (target > nums[mid]) {
        left = mid;
      } else {
        right = mid;
      }
    }
  }
};
