from random import randint


class RandomizedSet:

    def __init__(self):
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap[val] = None
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        self.hashmap.pop(val)
        return True

    def getRandom(self) -> int:
        options = list(self.hashmap.keys())
        value = randint(0, len(options) - 1)
        return options[value]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
