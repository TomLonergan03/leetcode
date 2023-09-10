class MyHashSet:

    def __init__(self):
        self.map = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        hash_key = key % 1000
        if key not in self.map[hash_key]:
            self.map[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = key % 1000
        if key in self.map[hash_key]:
            self.map[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        hash_key = key % 1000
        return key in self.map[hash_key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
