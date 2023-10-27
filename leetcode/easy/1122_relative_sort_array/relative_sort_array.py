from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_pos = {}
        for i in range(len(arr2)):
            arr2_pos[arr2[i]] = i
        remaining = []
        first_pass = []
        for i in range(len(arr1)):
            if arr1[i] not in arr2_pos:
                remaining.append(arr1[i])
            else:
                first_pass.append(arr1[i])
        first_pass = sorted(first_pass, key=lambda x: arr2_pos[x])
        return first_pass + sorted(remaining)
