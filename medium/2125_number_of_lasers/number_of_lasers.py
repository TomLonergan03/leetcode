from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = list(filter(lambda x: x != 0, map(
            lambda x: int(x, 2).bit_count(), bank)))
        lasers = 0
        for i in range(len(bank)-1):
            lasers += bank[i] * bank[i + 1]
        return lasers


bank = ["011001", "000000", "010100", "001000"]
sol = Solution()

print(sol.numberOfBeams(bank))
