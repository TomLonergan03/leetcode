# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    target = 6
    if num == target:
        return 0
    elif num > target:
        return -1
    else:
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        minimum = 0
        maximum = n
        while True:
            current_guess = minimum + (maximum - minimum + 1) // 2
            result = guess(current_guess)
            if result == 0:
                return current_guess
            elif result == 1:
                minimum = current_guess
            else:
                maximum = current_guess


print(Solution().guessNumber(10))
