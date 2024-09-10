#include <string>
#include <vector>

class Solution {
public:
  int evalRPN(std::vector<std::string> &tokens) {
    std::vector<int> stack;
    for (auto token : tokens) {
      if (token == "+") {
        int val1 = stack.back();
        stack.pop_back();
        int val2 = stack.back();
        stack.pop_back();
        stack.push_back(val2 + val1);
      } else if (token == "-") {
        int val1 = stack.back();
        stack.pop_back();
        int val2 = stack.back();
        stack.pop_back();
        stack.push_back(val2 - val1);
      } else if (token == "*") {
        int val1 = stack.back();
        stack.pop_back();
        int val2 = stack.back();
        stack.pop_back();
        stack.push_back(val2 * val1);
      } else if (token == "/") {
        int val1 = stack.back();
        stack.pop_back();
        int val2 = stack.back();
        stack.pop_back();
        stack.push_back(val2 / val1);
      } else {
        stack.push_back(stoi(token));
      }
    }
    return stack[0];
  }
};
