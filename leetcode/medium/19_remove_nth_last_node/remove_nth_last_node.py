from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node_front = head
        current_node_back = head
        i = 0
        while current_node_front.next != None:
            if i >= n:
                current_node_back = current_node_back.next
            current_node_front = current_node_front.next
            i += 1
        if i < n:
            return head.next
        current_node_back.next = current_node_back.next.next
        return head


print(Solution().removeNthFromEnd(ListNode(1, ListNode(2)), 1))
