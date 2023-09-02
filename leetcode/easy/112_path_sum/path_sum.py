# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.pathRecurse(root, targetSum, 0)

    def pathRecurse(self, node: TreeNode, targetSum: int, current_sum: int) -> bool:
        current_sum += node.val
        if node.left == None and node.right == None:
            if current_sum == targetSum:
                return True
            return False
        status = False
        if node.left != None:
            status = status or self.pathRecurse(
                node.left, targetSum, current_sum)
        if node.right != None:
            status = status or self.pathRecurse(
                node.right, targetSum, current_sum)
        return status
