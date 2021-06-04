import copy
from graph import Graph


def euler_check(cur_graph: Graph):
    oddCount = 0
    for node in cur_graph.nodes:
        oddCount += ((node.half_out - node.connected_to(node, True)) & 1)
    if oddCount != 0 and oddCount != 2:
        return False
    if cur_graph.get_connectivity_components_count() > 1:
        return False
    return True


def find_euler_path(cur_graph: Graph):
    res = []
    if len(cur_graph.nodes) == 0:
        return res

    if not euler_check(cur_graph):
        return "Граф не является Эйлеровым!"

    graph = copy.copy(cur_graph.matrix)

    graph = list(map(lambda row: list(map(lambda e: -1 if e[1] == 0 else e[0], enumerate(row))), graph))
    graph = list(map(lambda row: list(filter(lambda e: e != -1, row)), graph))

    for i, row in enumerate(graph):
        if (len(row) - row.count(i)) & 1:
            stack_nodes = [[i, graph[i]]]
            break
    else:
        stack_nodes = [[0, graph[0]]]

    while not (len(stack_nodes) == 0):
        cur = stack_nodes[-1]
        if len(cur[1]) == 0:
            res.append(stack_nodes.pop()[0])
        else:
            vert_ind = cur[1].pop()
            if vert_ind != cur[0]:
                graph[vert_ind].remove(cur[0])
            stack_nodes.append([vert_ind, graph[vert_ind]])
    return res
