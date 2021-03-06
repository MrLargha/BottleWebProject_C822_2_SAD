import copy
import string
from GraphNode import GraphNode
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import uuid


class Graph:
    @staticmethod
    def __deep_search(start_node: GraphNode):
        start_node.visited = True
        for node, _ in start_node.edges:
            if not node.visited and node is not start_node:
                Graph.__deep_search(node)

    """Получить заглавные буквы для названий вершин"""
    @staticmethod
    def get_nodes_names(count):
        return string.ascii_uppercase[:count]

    """Создать граф из пути"""
    @staticmethod
    def create_from_path(path):
        count = max(path) + 1
        mat = np.zeros((count, count), dtype=int)
        l = path[0]
        for e in path[1:]:
            mat[l][e] = 1
            l = e
        return Graph(mat)

    def __init__(self, adjacency_matrix):
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

    """Стереть метаданные"""
    def reset_metadata(self):
        for node in self.nodes:
            node.metadata = []

    """Вернуть количество компонент связности"""
    def get_connectivity_components_count(self):
        components = 0
        new_nodes = self.nodes
        while len(new_nodes) != 0:
            Graph.__deep_search(new_nodes[0])
            new_nodes = list(filter(lambda x: not x.visited, self.nodes))
            components += 1
        self.reset_visited()
        return components

    """Сохранить граф в файл"""
    def save_to_file(self, size_of_node=3000, size=12, edge_colors=None):
        if edge_colors is None:
            edge_colors = ['r']
        G = nx.DiGraph()
        if len(self.nodes) == 1 and not self.nodes[0].connected_to(self.nodes[0], True):
            G.add_node(self.nodes[0].name)
        else:
            G.add_edges_from(self.get_edges_by_pairs())
        pos = nx.shell_layout(G)
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=size_of_node, node_color='#8bc34a')
        nx.draw_networkx_labels(G, pos, font_size=size)
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, arrows=self.oriented)
        filename = '.\\static\\' + str(uuid.uuid1()).replace('-', '') + '.png'
        fig: plt.Figure = plt.gcf()
        fig.set_size_inches(12, 12)
        plt.savefig(filename, format="PNG", )
        plt.clf()
        return filename

    """Получить вершины попарно, для неориентированного графа вершины не будут продублированы"""
    def get_edges_by_pairs(self):
        result = []
        for i, row in enumerate(self.matrix):
            for j, edge in enumerate(row):
                new_pair = (self.nodes[i].name, self.nodes[j].name)
                if edge > 0 and (self.oriented or (tuple(reversed(new_pair)) not in result)):
                    result.append(new_pair)
        return result


