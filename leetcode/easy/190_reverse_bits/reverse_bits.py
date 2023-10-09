class Solution:
    def reverseBits(self, n: int) -> int:
        return int("".join(list(reversed(format(n, '032b')))), 2)
