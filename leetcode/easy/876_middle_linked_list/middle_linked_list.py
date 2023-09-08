from typing import Optional

from math import ceil

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        length = 0
        while node != None:
            node = node.next
            length += 1
        mid = length // 2
        node = head
        for _ in range(mid):
            node = node.next
        return node
