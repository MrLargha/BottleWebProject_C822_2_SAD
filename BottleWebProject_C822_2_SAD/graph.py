import copy
import string
from typing import List
from GraphNode import GraphNode
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import uuid


class Graph:
    def __init__(self, adjacency_matrix: List[List[int]]):
        names = Graph.get_nodes_names(len(adjacency_matrix))
        self.nodes = [GraphNode(names[i]) for i in range(len(adjacency_matrix))]
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

    def euler_check(self):
        oddCount = 0
        for node in self.nodes:
            oddCount += (node.half_out & 1)
        if oddCount > 2:
            return False
        if self.get_connectivity_components_count() > 1:
            return False
        return True

    def find_euler_loop(self):
        res = []
        if len(self.nodes) == 0:
            return res

        if not self.euler_check():
            return "Граф не является эйлеровым"

        graph = copy.copy(self.matrix)

        graph = list(map(lambda row: list(map(lambda e: -1 if e[1] == 0 else e[0], enumerate(row))), graph))
        graph = list(map(lambda row: list(filter(lambda e: e != -1, row)), graph))

        stack_nodes = [[0, graph[0]]]
        for i, row in enumerate(graph):
            if len(row) & 1:
                stack_nodes[0] = [i, row]
                break

        while not (len(stack_nodes) == 0):
            cur = stack_nodes[len(stack_nodes) - 1]
            if len(cur[1]) == 0:
                res.append(stack_nodes.pop()[0])
            else:
                vert_ind = cur[1].pop()
                graph[vert_ind].remove(cur[0])
                stack_nodes.append([vert_ind, graph[vert_ind]])
        return res

    def save_to_file(self):
        G = nx.DiGraph()
        G.add_edges_from(self.get_edges_by_pairs())
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=500)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edge_color='r', arrows=self.oriented)
        filename = '.\\static\\' + str(uuid.uuid1()).replace('-', '') + '.png'
        plt.savefig(filename, format="PNG")
        return filename

    def get_edges_by_pairs(self):
        result = []
        for i, row in enumerate(self.matrix):
            for j, edge in enumerate(row):
                if edge > 0:
                    result.append((str(i + 1), str(j + 1)))
        return result

    @staticmethod
    def __deep_search(start_node: GraphNode):
        start_node.visited = True
        for node, _ in start_node.edges:
            if not node.visited and node is not start_node:
                Graph.__deep_search(node)

    @staticmethod
    def get_nodes_names(count):
        return string.ascii_uppercase[:count]


if __name__ == '__main__':
    # test_matrix = [[0, 1, 0, 0],
    #                [0, 0, 0, 0],
    #                [0, 0, 1, 0],
    #                [0, 0, 0, 1]]
    # test_matrix = [[1, 1, 0, 0, 1, 0],
    #                [1, 0, 1, 0, 1, 0],
    #                [0, 1, 0, 1, 0, 0],
    #                [0, 0, 1, 0, 1, 1],
    #                [1, 1, 0, 1, 0, 0],
    #                [0, 0, 0, 1, 0, 0]]
    test_matrix = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]

    g = Graph(test_matrix)
    g.save_to_file()
