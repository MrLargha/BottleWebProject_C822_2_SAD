from typing import List, Tuple


class GraphNode:
    def __init__(self, name):
        self.name = name
        self.edges: List[Tuple[GraphNode, int]] = []
        self.visited = False

        """Промежуточный буфер для широкого применения"""
        self.metadata = []

        """Степень полузахода, кол-во ребёр ВХОДЯЩИХ в вершину"""
        self.half_in = 0

        """Степень полуисхода, кол-во рёбер ВЫХОДЯЩИХ из вершины"""
        self.half_out = 0

    def add_edge(self, node: 'GraphNode', edge_len: int):
        self.edges.append((node, edge_len))
        self.half_out += 1

    def connected_to_all(self, nodes: List['GraphNode']):
        for edge in self.edges:
            if edge[0] not in nodes:
                return False
        return True

    # Имеет параметр self_looped_node для определения возможности наличия петель в графе
    def connected_to(self, node: 'GraphNode', self_looped_node=False):
        for edge in self.edges:
            if edge[0] == node and (self_looped_node or self != node):
                return True
        return False

    def __str__(self):
        return "Node " + str(self.name)

    def __repr__(self):
        return "Node " + str(self.name)
