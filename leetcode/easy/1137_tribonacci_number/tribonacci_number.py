class Solution:
    previous = {}

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n in self.previous:
            return self.previous[n]
        number = self.tribonacci(
            n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        self.previous[n] = number
        return number
