class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        n += 1
        ways_to_step = [None] * n
        print(ways_to_step)
        print(ways_to_step)
        ways_to_step[0] = 1
        ways_to_step[1] = 1

        for i in range(2, n):
            ways_to_step[i] = ways_to_step[i - 1] + ways_to_step[i - 2]
        return ways_to_step[-1]


print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
