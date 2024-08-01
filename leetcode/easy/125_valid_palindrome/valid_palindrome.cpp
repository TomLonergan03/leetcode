#include <string>

class Solution {
public:
  bool isPalindrome(std::string s) {
    std::string processed_s = "";
    for (auto c : s) {
      if (isalnum(c)) {
        processed_s += tolower(c);
      }
    }
    if (processed_s.size() == 0) {
      return true;
    }
    auto start = 0;
    auto end = processed_s.size() - 1;
    while (start < end) {
      if (processed_s[start] != processed_s[end]) {
        return false;
      }
      start++;
      end--;
    }
    return true;
  }
};
