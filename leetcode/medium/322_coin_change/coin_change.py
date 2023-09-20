from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins_to_make = [10**5] * (amount + 1)
        coins_to_make[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                previous = i - coin
                if previous < 0:
                    continue
                if coins_to_make[previous] == -1:
                    continue
                coins_to_make[i] = min(
                    coins_to_make[i], coins_to_make[previous] + 1)
            if coins_to_make[i] == 10**5:
                coins_to_make[i] = -1
        return coins_to_make[-1]


print(Solution().coinChange([1, 2, 5], 11))
