from graph import Graph, GraphNode


# Проверить граф на полноту
def check_full(graph: Graph):
    for i, node in enumerate(graph.nodes):
        if len(node.edges) < len(graph.nodes) - 1:
            return False
    return True


# Вывести вхождения подграфа в граф
def find(origin_graph, graph_to_search):
    raise

