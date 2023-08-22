class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_word = {}
        word_to_pattern = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(words)):
            if pattern[i] in pattern_to_word:
                if pattern_to_word[pattern[i]] != words[i]:
                    return False
            if words[i] in word_to_pattern:
                if word_to_pattern[words[i]] != pattern[i]:
                    return False
            else:
                pattern_to_word[pattern[i]] = words[i]
                word_to_pattern[words[i]] = pattern[i]
        return True


print(Solution().wordPattern("abba", "dog cat cat dog"))
print(Solution().wordPattern("abba", "dog dog dog dog"))
print(Solution().wordPattern("abc", "dog cat dog"))
