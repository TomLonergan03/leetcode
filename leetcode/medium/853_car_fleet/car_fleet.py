from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars = sorted(cars, key=lambda x: x[0])
        time_to_finish = list(map(lambda x: (target - x[0]) / x[1], cars))
        current_min_time = time_to_finish[-1]
        for i in reversed(range(len(time_to_finish))):
            if time_to_finish[i] < current_min_time:
                time_to_finish[i] = current_min_time
            else:
                current_min_time = time_to_finish[i]
        return len(set(time_to_finish))


assert Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
assert Solution().carFleet(10, [8, 3, 7, 4, 6, 5], [4, 4, 4, 4, 4, 4]) == 6
assert Solution().carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
