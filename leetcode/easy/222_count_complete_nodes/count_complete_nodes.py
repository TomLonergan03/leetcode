from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left = self.findDepthLeft(root.left)
        right = self.findDepthRight(root.right)
        if left == right:
            return 2 ** left - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def findDepthLeft(self, node):
        height = 1
        while node:
            height += 1
            node = node.left
        return height

    def findDepthRight(self, node):
        height = 1
        while node:
            height += 1
            node = node.right
        return height
