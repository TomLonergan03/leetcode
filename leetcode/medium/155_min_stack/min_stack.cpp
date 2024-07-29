#include <vector>

class MinStack {
public:
  MinStack() {}

  void push(int val) {
    stack.push_back(val);
    if (min_stack.size() == 0 || val <= min_stack.back()) {
      min_stack.push_back(val);
    }
  }

  void pop() {
    if (stack.back() == min_stack.back()) {
      min_stack.pop_back();
    }
    stack.pop_back();
  }

  int top() { return stack.back(); }

  int getMin() { return min_stack.back(); }

private:
  std::vector<int> stack;
  std::vector<int> min_stack;
};
