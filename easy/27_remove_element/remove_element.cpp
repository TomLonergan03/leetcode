#include <vector>

int main(int argc, char const *argv[]) {
  /* code */
  return 0;
}

class Solution {
public:
  int removeElement(std::vector<int> &nums, int val) {
    int read = 0;
    int write = 0;
    int number_remaining = 0;
    for (std::size_t i = 0; i < nums.size(); i++) {
      if (nums[i] == val) {
        read++;
        continue;
      }
      nums[write] = nums[read];
      write++;
      read++;
      number_remaining++;
    }
    return number_remaining;
  }
};