import copy
import random
from typing import List
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


find(big_graph)
print("Found " + str(len(clicks)) + " clicks:")
print(clicks)

clicks5 = list(filter(lambda x: len(x) == 5, clicks))

print("Found " + str(len(clicks5)) + " 5-size clicks:")
print(clicks5)
