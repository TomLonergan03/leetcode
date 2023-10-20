class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.max_size = k
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.tail % self.max_size] = value
        self.tail += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head += 1
        return True

    def Front(self) -> int:
        if self.head == self.tail:
            return -1
        return self.queue[self.head % self.max_size]

    def Rear(self) -> int:
        if self.head == self.tail:
            return -1
        return self.queue[(self.tail - 1) % self.max_size]

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        return not self.isEmpty() and (self.tail - self.head) % self.max_size == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
