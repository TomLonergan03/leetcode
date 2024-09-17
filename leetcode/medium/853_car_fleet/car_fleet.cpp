#include <algorithm>
#include <cstdio>
#include <unordered_set>
#include <utility>
#include <vector>

class Solution {
public:
  int carFleet(int target, std::vector<int> &position,
               std::vector<int> &speed) {
    std::vector<std::pair<int, int>> cars;
    for (int i = 0; i < position.size(); i++) {
      cars.emplace_back(position[i], speed[i]);
    }
    std::sort(cars.begin(), cars.end(),
              [](std::pair<int, int> a, std::pair<int, int> b) {
                return a.first < b.first;
              });
    std::vector<float> time_to_finish;
    for (auto car : cars) {
      auto ttf = ((float)target - car.first) / car.second;
      time_to_finish.push_back(((float)target - car.first) / car.second);
    }
    float current_min_time = time_to_finish[time_to_finish.size() - 1];
    for (int i = time_to_finish.size() - 1; i >= 0; i--) {
      if (time_to_finish[i] < current_min_time) {
        time_to_finish[i] = current_min_time;
      } else {
        current_min_time = time_to_finish[i];
      }
    }
    return std::unordered_set<float>(time_to_finish.begin(),
                                     time_to_finish.end())
        .size();
  }
};
