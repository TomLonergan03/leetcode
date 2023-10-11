# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version == 4:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.binarySearch(0, n)

    def binarySearch(self, start, end):
        if end - start == 1:
            return end
        mid = start + (end - start) // 2
        if isBadVersion(mid):
            return self.binarySearch(start, mid)
        else:
            return self.binarySearch(mid, end)


print(Solution().firstBadVersion(5))
