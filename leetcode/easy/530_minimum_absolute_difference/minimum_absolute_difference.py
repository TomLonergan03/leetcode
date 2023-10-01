from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    vals = []

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.recurse(root)
        self.vals = sorted(self.vals)
        print(self.vals)
        return self.vals[1] - self.vals[0]

    def recurse(self, node):
        self.vals.append(node.val)
        if node.left:
            self.recurse(node.left)
        if node.right:
            self.recurse(node.right)


print(Solution().getMinimumDifference(
    TreeNode(1, None, TreeNode(5, TreeNode(3)))))
