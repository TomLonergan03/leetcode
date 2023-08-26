from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        result_current_position = result
        while True:
            if list1 == None and list2 == None:
                # first result node is a placeholder
                return result.next
            elif list1 == None:
                result_current_position.next = list2
                list2 = list2.next
            elif list2 == None:
                result_current_position.next = list1
                list1 = list1.next
            else:
                if list2.val < list1.val:
                    result_current_position.next = list2
                    list2 = list2.next
                else:
                    result_current_position.next = list1
                    list1 = list1.next
            result_current_position = result_current_position.next
