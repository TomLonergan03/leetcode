class Node:
    def __init__(self, key, val, next=None, previous=None):
        self.key = key
        self.val = val
        self.next = next
        self.previous = previous


class LRUCache:

    def __init__(self, capacity: int):
        self.maxlen = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        target = self.cache[key]
        self.front(target)
        return target.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.front(self.cache[key])
        else:
            self.cache[key] = Node(key, value, self.head)
            self.head = self.cache[key]
            if self.head.next:
                self.head.next.previous = self.head
            if len(self.cache) > self.maxlen:
                evict = self.tail
                if evict.previous.next:
                    evict.previous.next = None
                self.tail = evict.previous
                self.cache.pop(evict.key)
        if len(self.cache) == 1:
            self.tail = self.head

    def front(self, node):
        if node == self.head:
            return
        if node == self.tail:
            node.next = self.head
            self.head.previous = node
            self.head = node
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            node.previous.next = node.next
            if node.next:
                node.next.previous = node.previous
            node.next = self.head
            node.next.previous = node
            node.previous = None
            self.head = node


cache = LRUCache(3)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
cache.put(4, 4)
print(cache.get(4))
print(cache.get(3))
print(cache.get(2))
print(cache.get(1))
cache.put(5, 5)
print(cache.get(1))
print(cache.get(2))
print(cache.get(3))
print(cache.get(4))
print(cache.get(5))
