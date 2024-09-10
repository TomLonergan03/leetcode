#include <unordered_set>
#include <vector>

class Solution {
public:
  int longestConsecutive(std::vector<int> &nums) {
    std::unordered_set<int> nums_set(nums.begin(), nums.end());
    int max = 0;
    for (auto num : nums) {
      if (nums_set.find(num - 1) != nums_set.end()) {
        continue;
      }
      int curr = num;
      while (nums_set.find(curr) != nums_set.end()) {
        curr++;
      }
      max = std::max(max, curr - num);
    }
    return max;
  }
};
