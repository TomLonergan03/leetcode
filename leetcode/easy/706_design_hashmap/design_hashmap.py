class MyHashMap:

    def __init__(self):
        self.map = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % 1000
        for i in range(len(self.map[hash_key])):
            if self.map[hash_key][i][0] == key:
                self.map[hash_key][i] = (key, value)
                return
        self.map[hash_key].append((key, value))

    def get(self, key: int) -> int:
        hash_key = key % 1000
        for map_key, value in self.map[hash_key]:
            if map_key == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        hash_key = key % 1000
        for map_key, value in self.map[hash_key]:
            if map_key == key:
                self.map[hash_key].remove((key, value))


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
