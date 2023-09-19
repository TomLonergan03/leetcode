from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.level_sum = [0] * self.findDepth(root)
        self.level_count = [0] * self.findDepth(root)
        self.recurse(root, 0)
        result = []
        for i in range(len(self.level_count)):
            result.append(self.level_sum[i] / self.level_count[i])
        return result

    def findDepth(self, node):
        if node == None:
            return 0
        left = self.findDepth(node.left)
        right = self.findDepth(node.right)
        return max(left, right) + 1

    def recurse(self, node, level):
        if node == None:
            return
        self.level_sum[level] += node.val
        self.level_count[level] += 1
        self.recurse(node.left, level + 1)
        self.recurse(node.right, level + 1)
