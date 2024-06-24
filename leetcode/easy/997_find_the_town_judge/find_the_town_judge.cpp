#include <vector>

class Solution {
public:
  int findJudge(int n, std::vector<std::vector<int>> &trust) {
    std::vector<std::pair<int, int>> trust_count(n, std::make_pair(0, 0));
    for (auto pair : trust) {
      trust_count[pair[0] - 1].first++;
      trust_count[pair[1] - 1].second++;
    }
    for (int i = 0; i < n; i++) {
      if (trust_count[i].first == 0 && trust_count[i].second == n - 1) {
        return i + 1;
      }
    }
    return -1;
  }
};
