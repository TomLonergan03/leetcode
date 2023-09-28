from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_from = [None for _ in range(len(cost))]
        cost_from[0] = cost[0]
        cost_from[1] = cost[1]
        for i in range(2, len(cost)):
            cost_from[i] = min(cost_from[i - 1], cost_from[i - 2]) + cost[i]
        return min(cost_from[-1], cost_from[-2])


print(Solution().minCostClimbingStairs([10, 15, 20]))
