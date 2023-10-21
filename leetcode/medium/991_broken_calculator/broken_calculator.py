class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        steps = 0
        if target < startValue:
            return startValue - target
        while target != startValue:
            steps += 1
            if target % 2 == 0 and target > startValue:
                target /= 2
            else:
                target += 1
        return steps


print(Solution().brokenCalc(2, 3))
print(Solution().brokenCalc(5, 8))
print(Solution().brokenCalc(3, 10))
