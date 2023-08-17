from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        ranges = []
        range_start = nums[0]
        range_end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == range_end + 1:
                range_end += 1
                continue
            if range_start == range_end:
                ranges.append(str(range_start))
            else:
                ranges.append(str(range_start) + "->" + str(range_end))
            range_start = nums[i]
            range_end = nums[i]
        if range_start == range_end:
            ranges.append(str(range_start))
        else:
            ranges.append(str(range_start) + "->" + str(range_end))
        return ranges


if __name__ == "__main__":
    print("[0, 1, 2, 4, 5, 7]", Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
    print("[0, 2, 3, 4, 6, 8, 9]",
          Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]))
    print("[]", Solution().summaryRanges([]))
