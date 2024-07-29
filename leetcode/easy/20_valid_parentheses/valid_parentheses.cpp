#include <string>
#include <vector>

class Solution {
public:
  bool isValid(std::string s) {
    std::vector<char> stack;
    auto curr = 0;
    while (curr < s.length()) {
      if (s[curr] == '(' || s[curr] == '{' || s[curr] == '[') {
        stack.push_back(s[curr]);
        curr++;
      } else if (stack.size() > 0 &&
                 (stack[stack.size() - 1] == '(' && s[curr] == ')' ||
                  stack[stack.size() - 1] == '[' && s[curr] == ']' ||
                  stack[stack.size() - 1] == '{' && s[curr] == '}')) {
        curr++;
        stack.pop_back();
      } else {
        return false;
      }
    }
    return stack.size() == 0;
  }
};
