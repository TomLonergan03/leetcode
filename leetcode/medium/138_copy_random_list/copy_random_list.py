from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        new_head = Node(head.val)
        # map of old nodes to new nodes
        nodes = {head: new_head}
        node = head.next
        new_tail = new_head
        # copy each node in list without dealing with random
        while node:
            new_node = Node(node.val)
            nodes[node] = new_node
            new_tail.next = new_node
            new_tail = new_node
            node = node.next
        # link up all random pointers
        node = head
        while node:
            if node.random:
                nodes[node].random = nodes[node.random]
            node = node.next
        return new_head


ll = Node(1)
ll.next = Node(2, None, ll)
ll.random = ll
Solution().copyRandomList(ll)
