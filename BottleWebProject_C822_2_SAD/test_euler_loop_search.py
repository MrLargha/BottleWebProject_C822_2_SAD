from unittest import TestCase
from graph import Graph
from euler_loop_search import euler_check


class TestSearch(TestCase):
    def __init__(self, method_name="runEulerLoopTest"):
        self.one_vertex_graph = Graph([[1]])
        self.loop_graph = Graph([[1, 1, 1],
                                 [1, 1, 1],
                                 [1, 1, 1]])
        self.right_graph = Graph([[0, 1, 1, 0, 1, 1],
                                  [1, 0, 1, 1, 1, 0],
                                  [1, 1, 0, 1, 1, 0],
                                  [0, 1, 1, 0, 1, 1],
                                  [1, 1, 1, 1, 0, 0],
                                  [1, 0, 0, 1, 0, 0]])
        self.graph_with_two_odd_degree_vertex = Graph([[0, 1, 1, 0, 1, 1],
                                                       [1, 0, 1, 1, 1, 0],
                                                       [1, 1, 0, 1, 1, 0],
                                                       [0, 1, 1, 0, 1, 1],
                                                       [1, 1, 1, 1, 0, 1],
                                                       [1, 0, 0, 1, 1, 0]])
        self.graph_with_two_connectivity_components = Graph([[0, 1, 1, 0, 1, 0],
                                                             [1, 0, 1, 1, 1, 0],
                                                             [1, 1, 0, 1, 1, 0],
                                                             [0, 1, 1, 0, 1, 0],
                                                             [1, 1, 1, 1, 0, 0],
                                                             [0, 0, 0, 0, 0, 0]])
        super().__init__(methodName=method_name)

    def test_find_euler_loop(self):
        self.assertTrue(euler_check(self.one_vertex_graph))
        self.assertTrue(euler_check(self.loop_graph))
        self.assertTrue(euler_check(self.right_graph))
        self.assertFalse(euler_check(self.graph_with_two_odd_degree_vertex))
        self.assertFalse(euler_check(self.graph_with_two_connectivity_components))
