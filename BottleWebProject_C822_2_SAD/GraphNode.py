from typing import List, Tuple
from typing import TypeVar


class GraphNode:
    def __init__(self, name):
        self.name = name
        self.edges: List[Tuple[GraphNode, int]] = []
        self.visited = False

    def add_edge(self, node: 'GraphNode', edge_len: int):
        self.edges.append((node, edge_len))

    def __str__(self):
        return "Node " + str(self.name)

    def __repr__(self):
        return "Node " + str(self.name)