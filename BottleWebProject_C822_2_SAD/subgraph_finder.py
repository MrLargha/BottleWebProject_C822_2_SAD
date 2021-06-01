import copy
from datetime import datetime
from typing import List
from bottle import route, post, template, request
import request_utils
from graph import Graph, GraphNode

big_graph = Graph([[0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
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
click_colors = ['#fc1100', '#ffea00', '#07f52b', '#6ed4d2', '#031682', '#9d0be6', '#ff05e2', '#730813',
                '#7d3102', '#588061']


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
        if len(new_not_candidates) == 0 and len(new_candidates) == 0:
            clicks.append(compsub.copy())
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
    c = big_graph.nodes.copy()
    while len(c) > 0:
        extend(c, [])
    compsub.clear()


@post('/subgraph_search', method='post')
def search():
    matrix_dim = int(request.forms.get("MATRIX"))
    return template('enter_matrix', title='Поиск подграфа в графе',
                    message='Задача Андрея Богданова на поиск подграфа в графе',
                    year=datetime.now().year, rows=matrix_dim, columns=matrix_dim,
                    names=Graph.get_nodes_names(matrix_dim),
                    callback='subgraph_matrix_entered',
                    yarus=-1)


@post('/subgraph_matrix_entered', method='post')
def solve():
    matrix = request_utils.extract_matrix_from_request_params(request.forms)
    # g = Graph(matrix)
    g = big_graph
    find(g)
    result = list(filter(lambda x: len(x) == 5, clicks.copy()))
    clicks.clear()
    print(result)
    edges = g.get_edges_by_pairs()
    colors = []
    for edge1, edge2 in edges:
        color = '#000000'
        for i, click in enumerate(result):
            color_n = i % len(click_colors)
            if edge1 in map(lambda x: x.name, click) and edge2 in map(lambda x: x.name, click):
                color = click_colors[color_n]
        colors.append(color)
    for i, click in enumerate(result):
        for node in click:
            if 'SG' not in node.name:
                node.name += "\nSG:"
            node.name += ' ' + str(i) + ';'
    path = g.save_to_file(colors)
    return template('subgraph_view', title='Результат поиска подгафов', subgraph_count=len(result),
                    image_path=path)
