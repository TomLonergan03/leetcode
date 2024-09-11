#include <cstdio>
#include <string>
#include <vector>

class Solution {
public:
  std::vector<std::string> generateParenthesis(int n) {
    dfs(0, 0, "", n);
    return list;
  }

private:
  void dfs(int left, int right, std::string current, int n) {
    if (left == n && right == n) {
      list.push_back(current);
      return;
    }
    if (left < n) {
      std::string next(current + "(");
      dfs(left + 1, right, next, n);
    }
    if (right < left) {
      std::string next(current + ")");
      dfs(left, right + 1, next, n);
    }
  }

  std::vector<std::string> list;
};
