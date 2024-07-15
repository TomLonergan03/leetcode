#include <string>
#include <unordered_map>

class Solution {
public:
  bool isAnagram(std::string s, std::string t) {
    if (s.length() != t.length()) {
      return false;
    }
    std::unordered_map<char, int> s_count{};
    std::unordered_map<char, int> t_count{};
    for (int i = 0; i < s.length(); i++) {
      if (s_count.find(s[i]) == s_count.end()) {
        s_count.emplace(std::pair<char, int>{s[i], 1});
      } else {
        s_count[s[i]] += 1;
      }
      if (t_count.find(t[i]) == t_count.end()) {
        t_count.emplace(std::pair<char, int>{t[i], 1});
      } else {
        t_count[t[i]] += 1;
      }
    }
    for (int i = 0; i < s.length(); i++) {
      auto maybe_s = s_count.find(s[i]);
      auto maybe_t = t_count.find(s[i]);
      if (maybe_s == s_count.end() || maybe_t == t_count.end()) {
        return false;
      }
      if (maybe_s->second != maybe_t->second) {
        return false;
      }
    }
    return true;
  }
};
