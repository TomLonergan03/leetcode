class MinStack:

    def __init__(self):
        self.values = []
        self.min_with = []
        self.top_index = -1

    def push(self, val: int) -> None:
        self.values.append(val)
        if len(self.min_with) == 0:
            self.min_with.append(val)
        else:
            self.min_with.append(
                min(val, self.min_with[max(self.top_index, 0)]))
        self.top_index += 1

    def pop(self) -> None:
        self.values.pop()
        self.min_with.pop()
        self.top_index -= 1

    def top(self) -> int:
        return self.values[self.top_index]

    def getMin(self) -> int:
        return self.min_with[self.top_index]
