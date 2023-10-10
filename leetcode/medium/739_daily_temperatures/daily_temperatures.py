from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        wait = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                wait[index] = i - index
            stack.append(i)
        return wait
