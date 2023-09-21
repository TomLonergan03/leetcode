from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        current = head
        to_remove = set()
        while current.next != None:
            if current.val == current.next.val:
                to_remove.add(current.val)
            current = current.next
        current = head
        while current != None:
            while current.next != None and current.next.val in to_remove:
                current.next = current.next.next
            current = current.next
        if head.val in to_remove:
            return head.next
        return head
