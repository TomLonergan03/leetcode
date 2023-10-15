from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.values = []
        self.recurse(root)
        return self.values

    def recurse(self, node):
        self.values.append(node.val)
        if node.left:
            self.recurse(node.left)
        if node.right:
            self.recurse(node.right)
