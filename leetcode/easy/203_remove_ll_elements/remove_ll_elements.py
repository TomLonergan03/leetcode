from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        current = head
        while current:
            while current.next and current.next.val == val:
                current.next = current.next.next
            current = current.next
        return head


Solution().removeElements(ListNode(7, ListNode(7, ListNode(7, ListNode(7)))), 7)
