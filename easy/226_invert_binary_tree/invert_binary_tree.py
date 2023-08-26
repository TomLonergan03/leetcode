# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recurse(root)
        return root

    def recurse(self, node):
        if node == None:
            return
        temp = node.left
        node.left = node.right
        node.right = temp
        self.recurse(node.left)
        self.recurse(node.right)
