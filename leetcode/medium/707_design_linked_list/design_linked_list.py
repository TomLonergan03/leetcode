class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def get(self, index: int) -> int:
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.val
            current = current.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        if self.len == 0:
            self.tail = self.head
        self.len += 1

    def addAtTail(self, val: int) -> None:
        if self.len == 0:
            self.addAtHead(val)
            return
        self.len += 1
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.len:
            self.addAtTail(val)
            return
        current = self.head
        previous = current
        i = 0
        while current:
            if i == index:
                previous.next = Node(val, current)
                self.len += 1
                break
            previous = current
            current = current.next
            i += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.len > 0:
            self.head = self.head.next
            self.len -= 1
            return
        current = self.head
        previous = current
        i = 0
        while current:
            if i == index:
                self.len -= 1
                previous.next = current.next
                if current == self.tail:
                    self.tail = previous
                break
            previous = current
            current = current.next
            i += 1


obj = MyLinkedList()
obj.addAtTail(1)
obj.addAtTail(3)
print(obj.get(1))
