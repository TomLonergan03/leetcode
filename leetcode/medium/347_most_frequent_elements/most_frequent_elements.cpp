#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<int> topKFrequent(std::vector<int> &nums, int k) {
    std::unordered_map<int, int> counts;
    for (auto &num : nums) {
      auto maybe_num = counts.find(num);
      if (maybe_num == counts.end()) {
        counts.insert({num, 1});
      } else {
        maybe_num->second++;
      }
    }
    std::vector<std::pair<int, int>> count_pairs;
    for (auto &kv : counts) {
      count_pairs.push_back(kv);
    }
    std::sort(count_pairs.begin(), count_pairs.end(),
              [](std::pair<int, int> x, std::pair<int, int> y) {
                return x.second > y.second;
              });
    auto result_pairs =
        std::vector(count_pairs.begin(), count_pairs.begin() + k);
    std::vector<int> result;
    for (auto &pair : result_pairs) {
      result.push_back(pair.first);
    }
    return result;
  }
};
