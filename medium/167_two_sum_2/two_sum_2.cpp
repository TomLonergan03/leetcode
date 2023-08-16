#include <iostream>
#include <vector>

class Solution {
public:
  std::vector<int> twoSum(std::vector<int> &numbers, int target) {
    int left = 0;
    int right = numbers.size() - 1;

    while (true) {
      const int sum = numbers[left] + numbers[right];
      if (sum == target) {
        std::vector<int> result{left + 1, right + 1};
        return result;
      }
      if (sum < target) {
        left++;
      } else {
        right--;
      }
    }
  }
};

int main(int argc, char const *argv[]) {
  std::vector<int> numbers{2, 7, 11, 15};
  auto result = Solution().twoSum(numbers, 9);
  for (int element : result) {
    std::cout << element << " ";
  }
  std::cout << std::endl;
  return 0;
}
