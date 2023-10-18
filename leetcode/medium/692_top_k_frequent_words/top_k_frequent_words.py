from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return list(map(lambda x: x[0], list(sorted(
            sorted(Counter(words).items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True))[:k]))
