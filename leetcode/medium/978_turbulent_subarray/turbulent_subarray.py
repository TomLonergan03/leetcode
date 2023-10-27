from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        current_length = 1
        if arr[0] != arr[1]:
            current_length += 1
        max_length = current_length
        previous_change = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            next_change = arr[i + 1] - arr[i]
            if next_change * previous_change < 0:
                current_length += 1
            else:
                current_length = 1
                if next_change:
                    current_length += 1
            max_length = max(max_length, current_length)
            previous_change = next_change
        return max_length
