from pyparsing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.recurse(root, 1)

    def recurse(self, node: Optional[TreeNode], current_depth: int) -> int:
        if node == None:
            return 10**6
        if node.left == None and node.right == None:
            return current_depth
        left = self.recurse(node.left, current_depth + 1)
        right = self.recurse(node.right, current_depth + 1)
        return min(left, right)
