from typing import List, Tuple
from typing import TypeVar


class GraphNode:
    def __init__(self, name):
        self.name = int(name) - 1
        self.edges: List[Tuple[GraphNode, int]] = []
        self.visited = False

        """Помойка для хранения страшной алгоритмической ерунды"""
        self.metadata = []

        """Степень полузахода, кол-во ребёр ВХОДЯЩИХ в вершину"""
        self.half_in = 0

        """Степень полуисхода, кол-во рёбер ВЫХОДЯЩИХ из вершины"""
        self.half_out = len(self.edges)

    def add_edge(self, node: 'GraphNode', edge_len: int):
        self.edges.append((node, edge_len))

    def connected_to_all(self, nodes: List['GraphNode']):
        for edge in self.edges:
            if edge[0] not in nodes:
                return False
        return True

    def connected_to(self, node: 'GraphNode'):
        for edge in self.edges:
            if edge[0] == node:
                return True
        return False

    def __str__(self):
        return "Node " + str(self.name)

    def __repr__(self):
        return "Node " + str(self.name)

