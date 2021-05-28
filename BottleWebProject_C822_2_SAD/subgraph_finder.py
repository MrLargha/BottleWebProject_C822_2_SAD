import copy
import random
from datetime import datetime
from typing import List

from bottle import route, post, template, request

import request_utils
from graph import Graph, GraphNode

big_graph = Graph([[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                   [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                   [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
                   [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
                   [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                   [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
                   [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                   [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
                   [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0]])

compsub: List[GraphNode] = []
clicks: List[List[GraphNode]] = []


def contains_all_connected(target: List[GraphNode], search_in: List[GraphNode]):
    if not len(target):
        return False
    for node in target:
        if not node.connected_to_all(search_in):
            return False
    return True


def extend(candidates: List[GraphNode], not_candidates: List[GraphNode]):
    print("Next call")
    while len(candidates) > 0 and not contains_all_connected(not_candidates, candidates):
        print("Next iter")
        v = candidates[0]
        compsub.append(v)
        new_candidates = list(filter(lambda node: node.connected_to(v), candidates))
        new_not_candidates = list(filter(lambda node: node.connected_to(v), not_candidates))
        print(compsub)
        if len(new_not_candidates) == 0 and len(new_candidates) == 0:
            clicks.append(copy.copy(compsub))
            print("Click found" + str(clicks))
        else:
            extend(new_candidates, new_not_candidates)
        compsub.remove(v)
        candidates.remove(v)
        not_candidates.append(v)


# Проверить граф на полноту
def check_full(graph: Graph):
    for i, node in enumerate(graph.nodes):
        if len(node.edges) < len(graph.nodes) - 1:
            return False
    return True


# Вывести вхождения подграфа в граф
def find(origin_graph):
    c = origin_graph.nodes
    while len(c) > 0:
        extend(c, [])


@post('/subgraph_search', method='post')
def search():
    matrix_dim = int(request.forms.get("MATRIX"))
    return template('enter_matrix', title='Поиск подграфа в графе',
                    message='Задача Андрея Богданова на поиск подграфа в графе',
                    year=datetime.now().year, rows=matrix_dim, columns=matrix_dim,
                    names=Graph.get_nodes_names(matrix_dim))


@post('/subgraph_matrix_entered', method='post')
def solve():
    request_utils.extract_matrix_from_request_params(request.forms)