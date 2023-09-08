from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        assembled_word = ""
        for word in words:
            assembled_word += word
            if assembled_word == s:
                return True
        return False
