from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret = [char for char in secret]
        guess = [char for char in guess]
        bulls = len(list(filter(lambda x: x[0] == x[1], zip(
            secret, guess))))
        secret = Counter(secret)
        guess = Counter(guess)
        cows = 0
        for key in secret.keys():
            if key in guess:
                cows += min(secret[key], guess[key])
        cows -= bulls
        return str(bulls) + "A" + str(cows) + "B"
