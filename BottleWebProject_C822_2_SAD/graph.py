import copy
from typing import List
from GraphNode import GraphNode
import numpy as np


class Graph:
    def __init__(self, adjacency_matrix: List[List[int]]):
        self.nodes = [GraphNode(i + 1) for i in range(len(adjacency_matrix))]
        self.matrix = copy.copy(adjacency_matrix)
        for i, row in enumerate(adjacency_matrix):
            for j, edge in enumerate(row):
                if edge > 0:
                    self.nodes[i].add_edge(self.nodes[j], edge)
        for i, row in enumerate(np.array(self.matrix).T):
            self.nodes[i].half_in = len(list(filter(lambda x: x > 0, row)))
        self.oriented = not (np.array(adjacency_matrix) == np.array(adjacency_matrix).T).all()

    """Установить в false все отметки visited"""
    def reset_visited(self):
        for node in self.nodes:
            node.visited = False

    """Стереть метаданные """
    def reset_metadata(self):
        for node in self.nodes:
            node.metadata = []

    def get_connectivity_components_count(self):
        components = 0
        new_nodes = self.nodes
        while len(new_nodes) != 0:
            Graph.__deep_search(new_nodes[0])
            new_nodes = list(filter(lambda x: not x.visited, self.nodes))
            components += 1
        self.reset_visited()
        return components

    @staticmethod
    def __deep_search(start_node: GraphNode):
        start_node.visited = True
        for node, _ in start_node.edges:
            if not node.visited and node is not start_node:
                Graph.__deep_search(node)


# test_matrix = [[0, 1, 0, 0],
#                [0, 0, 0, 0],
#                [0, 0, 1, 0],
#                [0, 0, 0, 1]]
test_matrix = [[1, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]]
g = Graph(test_matrix)
print(g.get_connectivity_components_count())
