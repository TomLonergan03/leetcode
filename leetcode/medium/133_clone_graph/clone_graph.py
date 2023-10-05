from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    new_nodes = {}

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node == None:
            return None
        self.buildList(node)
        for new_node in self.new_nodes:
            self.connectNeighbours(new_node)
        return self.new_nodes[node]

    def buildList(self, node):
        if node not in self.new_nodes:
            new_node = Node(node.val)
            self.new_nodes[node] = new_node
            for neighbor in node.neighbors:
                self.buildList(neighbor)

    def connectNeighbours(self, node):
        for neighbor in node.neighbors:
            self.new_nodes[node].neighbors.append(self.new_nodes[neighbor])
