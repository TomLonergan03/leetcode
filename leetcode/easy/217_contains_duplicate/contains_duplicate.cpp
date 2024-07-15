#include <unordered_set>
#include <vector>

class Solution {
public:
  bool containsDuplicate(std::vector<int> &nums) {
    std::unordered_set<int> seen(nums.begin(), nums.end());
    return nums.size() != seen.size();
  }
};
