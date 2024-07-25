#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<int> twoSum(std::vector<int> &nums, int target) {
    std::unordered_map<int, std::vector<int>> map;
    for (auto i = 0; i < nums.size(); i++) {
      const auto match_loc = map.find(target - nums[i]);
      if (match_loc != map.end()) {
        return {i, match_loc->second[0]};
      }
      const auto insert_loc = map.find(nums[i]);
      if (insert_loc == map.end()) {
        const std::vector<int> v{i};
        map.emplace(nums[i], std::move(v));
      } else {
        insert_loc->second.push_back(i);
      }
    }
    return {};
  }
};
