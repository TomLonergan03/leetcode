class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("abc.Ba"))
    print(sol.isPalindrome("abcde"))
