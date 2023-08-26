# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        carry = 0
        result_current_position = result
        while True:
            if l1 == None and l2 == None:
                if carry == 1:
                    result_current_position.next = ListNode(1)
                # first node of result is a placeholder
                return result.next
            else:
                if l1 == None:
                    val1 = 0
                else:
                    val1 = l1.val
                    l1 = l1.next
                if l2 == None:
                    val2 = 0
                else:
                    val2 = l2.val
                    l2 = l2.next
                total = val1 + val2 + carry
                if total >= 10:
                    carry = 1
                    total %= 10
                else:
                    carry = 0
                result_current_position.next = ListNode(total)
                result_current_position = result_current_position.next
