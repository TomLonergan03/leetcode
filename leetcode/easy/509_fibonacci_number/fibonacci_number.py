class Solution:
    previous = {}
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in self.previous:
            return self.previous[n]
        number = self.fib(n - 1) + self.fib(n - 2)
        self.previous[n] = number
        return number