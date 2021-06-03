import copy
from datetime import datetime
from typing import List
from bottle import post, template, request
import request_utils
import task_logger
from graph import Graph, GraphNode
from task_logger import Logger


class ClickFinder:
    click_colors = ['#fc1100', '#ffea00', '#07f52b', '#6ed4d2', '#031682', '#9d0be6', '#ff05e2', '#730813',
                    '#7d3102', '#588061']

    @staticmethod
    def contains_all_connected(target: List[GraphNode], search_in: List[GraphNode]):
        if not len(target):
            return False
        for node in target:
            if not node.connected_to_all(search_in):
                return False
        return True

    def __init__(self, target_graph: Graph):
        self.graph = copy.copy(target_graph)
        self.compsub: List[GraphNode] = []
        self.clicks: List[List[GraphNode]] = []

    def extend(self, candidates: List[GraphNode], not_candidates: List[GraphNode]):
        while len(candidates) > 0 and not ClickFinder.contains_all_connected(not_candidates, candidates):
            v = candidates[0]
            self.compsub.append(v)
            new_candidates = list(filter(lambda node: node.connected_to(v), candidates))
            new_not_candidates = list(filter(lambda node: node.connected_to(v), not_candidates))
            if len(new_not_candidates) == 0 and len(new_candidates) == 0:
                if len(self.compsub) == 5:
                    self.clicks.append(self.compsub.copy())
                    print("Click found" + str(self.compsub))
            else:
                self.extend(new_candidates, new_not_candidates)
            self.compsub.remove(v)
            candidates.remove(v)
            not_candidates.append(v)

    def find_clicks(self):
        c = self.graph.nodes.copy()
        while len(c) > 0:
            self.extend(c, [])
        return self.clicks.copy()

    def save_result_to_file(self):
        colors = self.__get_edges_colors()
        self.__rename_nodes()
        return self.graph.save_to_file(edge_colors=colors)

    def __get_edges_colors(self):
        colors = []
        for edge1, edge2 in self.graph.get_edges_by_pairs():
            color = '#000000'
            for i, click in enumerate(self.clicks):
                color_n = i % len(ClickFinder.click_colors)
                if edge1 in map(lambda x: x.name, click) and edge2 in map(lambda x: x.name,
                                                                          click) and edge1 is not edge2:
                    color = ClickFinder.click_colors[color_n]
            colors.append(color)
        return colors

    def __rename_nodes(self):
        for j, click in enumerate(self.clicks):
            for node in click:
                if 'SG' not in node.name:
                    node.name += "\nSG:"
                node.name += ' ' + str(j + 1) + ';'


@post('/subgraph_search', method='post')
def search():
    try:
        matrix_dim = int(request.forms.get("MATRIX"))
    except ValueError:
        return template('error', message='Введите кол-во вершин в графе!')
    return template('enter_matrix', title='Поиск подграфа в графе',
                    message='Задача Андрея Богданова на поиск подграфа в графе',
                    year=datetime.now().year, rows=matrix_dim, columns=matrix_dim,
                    names=Graph.get_nodes_names(matrix_dim),
                    callback='subgraph_matrix_entered',
                    yarus=-1)


@post('/subgraph_matrix_entered', method='post')
def solve():
    matrix = request_utils.extract_matrix_from_request_params(request.forms)
    logger = Logger('subgraph.log')
    logger.push_log("Entered matrix: \n" + str(matrix).replace('[', '').replace(']', ''))
    logger.push_log("Searching for full graphs...")
    g = Graph(matrix)
    finder = ClickFinder(g)
    result = finder.find_clicks()
    print(result)
    logger.push_log("Full subgraphs: " + str(result))
    return template('subgraph_view', title='Результат поиска подграфов', subgraph_count=len(result),
                    image_path=finder.save_result_to_file(), clicks=result)
