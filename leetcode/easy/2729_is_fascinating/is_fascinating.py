class Solution:
    def isFascinating(self, n: int) -> bool:
        n = [*(str(n) + str(2 * n) + str(3 * n))]
        return len(n) == 9 and "0" not in set(n) and len(set(n)) == 9
