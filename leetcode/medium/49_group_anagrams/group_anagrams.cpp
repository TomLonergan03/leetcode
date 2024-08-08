#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<std::vector<std::string>>
  groupAnagrams(std::vector<std::string> &strs) {
    std::unordered_map<std::string, std::vector<std::string>> anagram_groups;
    std::vector<std::string> keys;
    for (auto &str : strs) {
      auto key = std::string(str.begin(), str.end());
      std::sort(key.begin(), key.end());
      const auto maybe_key = anagram_groups.find(key);
      if (maybe_key == anagram_groups.end()) {
        anagram_groups.insert({key, {str}});
        keys.push_back(key);
      } else {
        maybe_key->second.push_back(str);
      }
    }
    std::vector<std::vector<std::string>> result;
    for (auto &key : keys) {
      result.push_back(anagram_groups[key]);
    }
    return result;
  }
};
