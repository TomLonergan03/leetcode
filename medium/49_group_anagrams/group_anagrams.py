from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for str in strs:
            anagram_dict = tuple(sorted(self.createAnagramDict(str).items()))
            if anagram_dict not in anagrams:
                anagrams[anagram_dict] = [str]
            else:
                anagrams[anagram_dict].append(str)
        result = []
        for element in anagrams.values():
            result.append(element)
        return result

    def createAnagramDict(self, str):
        char_counts = {}
        for char in str:
            if not char in char_counts:
                char_counts[char] = 1
            else:
                char_counts[char] += 1
        return char_counts


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(Solution().groupAnagrams(["ddddddddddg", "dgggggggggg"]))
