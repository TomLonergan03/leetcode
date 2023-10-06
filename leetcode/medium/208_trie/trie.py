class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.children = {}
        self.end_of_word = False

    def addChild(self, child):
        self.children[child.val] = child

    def getChild(self, val):
        if val not in self.children:
            return None
        return self.children[val]


class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        self.insertRec(self.root, word)

    def insertRec(self, node, word):
        if len(word) == 0:
            node.end_of_word = True
            return
        child = node.getChild(word[0])
        if not child:
            child = Node(word[0])
            node.addChild(child)
        self.insertRec(child, word[1:])

    def search(self, word: str) -> bool:
        return self.searchRec(self.root, word)

    def searchRec(self, node, word):
        if len(word) == 0:
            return node.end_of_word
        child = node.getChild(word[0])
        if not child:
            return False
        return self.searchRec(child, word[1:])

    def startsWith(self, prefix: str) -> bool:
        return self.startsWithRec(self.root, prefix)

    def startsWithRec(self, node, prefix):
        if len(prefix) == 0:
            return True
        child = node.getChild(prefix[0])
        print(child)
        if not child:
            print(child)
            return False
        return self.startsWithRec(child, prefix[1:])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
