#include <stack>
#include <vector>

class Solution {
public:
  std::vector<int> dailyTemperatures(std::vector<int> &temperatures) {
    std::stack<std::pair<int, int>> temperature_and_day;
    std::vector<int> result(temperatures.size(), 0);
    for (int day = temperatures.size() - 1; day >= 0; day--) {
      while (!temperature_and_day.empty() &&
             temperature_and_day.top().first <= temperatures[day]) {
        temperature_and_day.pop();
      }
      result[day] = temperature_and_day.empty()
                        ? 0
                        : temperature_and_day.top().second - day;
      temperature_and_day.push({temperatures[day], day});
    }
    return result;
  }
};
