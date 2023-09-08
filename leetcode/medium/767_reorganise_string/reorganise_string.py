from heapq import heapify, heappop


class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        heap = [(-val, key) for key, val in counts.items()]
        heapify(heap)
        result = [""] * n
        i = 0
        while len(heap) > 0:
            count, char = heappop(heap)
            count = -count
            if 2 * count - 1 > n:
                return ""
            for _ in range(count):
                result[i] = char
                if i + 2 < n:
                    i += 2
                else:
                    i = 1
        return "".join(result)


print(Solution().reorganizeString("aab"))
