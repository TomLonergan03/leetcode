#include <vector>

class Solution {
public:
  int findMin(std::vector<int> &nums) {
    int low = 0;
    int high = nums.size() - 1;
    while (high - low > 0) {
      int mid = low + (high - low) / 2;
      if (nums[mid] > nums[mid + 1]) {
        return nums[mid + 1];
      }
      if (mid > 0 && nums[mid] < nums[mid - 1]) {
        return nums[mid];
      }
      if (nums[high] > nums[mid]) {
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }
    return nums[0];
  }
};
