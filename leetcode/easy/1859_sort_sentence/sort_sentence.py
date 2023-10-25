class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join(map(lambda x: x[0], sorted(map(lambda x: (x[:-1], int(x[-1])),
                                                       s.split()), key=lambda x: x[1])))
