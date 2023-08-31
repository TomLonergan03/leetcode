from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        indexes_to_drop = set()
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            for j in range(i + 1, len(intervals)):
                if intervals[j][0] <= end:
                    end = max(intervals[j][1], end)
                    indexes_to_drop.add(j)
                else:
                    break
            result.append([start, end])
        for index in sorted(list(indexes_to_drop), reverse=True):
            result.pop(index)
        return result


# print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# print(Solution().merge([[1, 4], [4, 5]]))
# print(Solution().merge([[1, 3]]))
print(Solution().merge([[1, 4], [0, 2], [3, 5]]))
