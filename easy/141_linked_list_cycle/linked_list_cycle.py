# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional


class ListNode:
    a = 0


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        have_seen = set()
        current_node = head
        while True:
            if current_node in have_seen:
                return True
            if current_node.next == None:
                return False
            have_seen.add(current_node)
            current_node = current_node.next
