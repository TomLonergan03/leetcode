#include <algorithm>
#include <array>
#include <cstddef>
#include <cstdio>
#include <string>

class Solution {
public:
  int lengthOfLongestSubstring(std::string s) {
    if (s.size() == 0) {
      return 0;
    }
    std::array<bool, 256> substring = {false};
    substring[s[0]] = true;
    std::size_t substring_length = 1;
    std::size_t left = 0;
    std::size_t right = 0;
    std::size_t max = 1;
    while (right < s.size() - 1) {
      right++;
      substring_length++;
      const auto next_char = s[right];
      while (substring[next_char]) {
        const auto removed_char = s[left];
        left++;
        substring_length--;
        substring[removed_char] = false;
      }
      substring[next_char] = true;
      max = std::max(max, substring_length);
    }
    return max;
  }
};
