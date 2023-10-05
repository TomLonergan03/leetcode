from typing import Optional
from sys import maxsize
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidSubtree(root, -maxsize, maxsize)

    def isValidSubtree(self, node, min_val, max_val):
        if not node:
            return True
        if node.val >= max_val or node.val <= min_val:
            return False
        return self.isValidSubtree(node.left, min_val, node.val) and self.isValidSubtree(node.right, node.val, max_val)
