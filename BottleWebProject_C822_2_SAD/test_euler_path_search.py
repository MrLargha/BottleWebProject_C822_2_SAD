from unittest import TestCase
from graph import Graph
from euler_path_search import euler_check, find_euler_path


class TestSearch(TestCase):
    def __init__(self, method_name="runEulerLoopTest"):
        self.one_vertex_graph = Graph([[0]])
        self.one_vertex_self_looped_graph = Graph([[1]])
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
        self.linear_path_graph = Graph([[0, 1, 0, 0],
                                        [1, 0, 1, 0],
                                        [0, 1, 0, 1],
                                        [0, 0, 1, 0]])
        self.two_connected_self_looped_vertexes = Graph([[1, 1],
                                                         [1, 1]])
        self.graph_with_two_connectivity_components = Graph([[0, 1, 1, 0, 1, 0],
                                                             [1, 0, 1, 1, 1, 0],
                                                             [1, 1, 0, 1, 1, 0],
                                                             [0, 1, 1, 0, 1, 0],
                                                             [1, 1, 1, 1, 0, 0],
                                                             [0, 0, 0, 0, 0, 0]])
        self.graph_with_four_odd_degree_vertex = Graph([[0, 1, 1, 1],
                                                        [1, 0, 1, 1],
                                                        [1, 1, 0, 1],
                                                        [1, 1, 1, 0]])

        super().__init__(methodName=method_name)

    def test_euler_check(self):
        self.assertTrue(euler_check(self.one_vertex_graph))
        self.assertTrue(euler_check(self.one_vertex_self_looped_graph))
        self.assertTrue(euler_check(self.loop_graph))
        self.assertTrue(euler_check(self.right_graph))
        self.assertTrue(euler_check(self.graph_with_two_odd_degree_vertex))
        self.assertTrue(euler_check(self.linear_path_graph))
        self.assertTrue(euler_check(self.two_connected_self_looped_vertexes))
        self.assertFalse(euler_check(self.graph_with_two_connectivity_components))
        self.assertFalse(euler_check(self.graph_with_four_odd_degree_vertex))

    def test_euler_path(self):
        euler_path = find_euler_path(self.one_vertex_graph)
        self.assertTrue(len(euler_path) == 1)
        euler_path = find_euler_path(self.one_vertex_self_looped_graph)
        self.assertTrue(len(euler_path) == 2 and euler_path[0] == euler_path[1])
        euler_path = find_euler_path(self.loop_graph)
        self.assertTrue(len(euler_path) == 7 and euler_path[0] == euler_path[-1])
        euler_path = find_euler_path(self.right_graph)
        self.assertTrue(len(euler_path) == 12 and euler_path[0] == euler_path[-1])
        euler_path = find_euler_path(self.graph_with_two_odd_degree_vertex)
        self.assertTrue(len(euler_path) == 13)
        euler_path = find_euler_path(self.linear_path_graph)
        self.assertTrue(len(euler_path) == 4)
        euler_path = find_euler_path(self.two_connected_self_looped_vertexes)
        self.assertTrue(len(euler_path) == 4)

# if __name__ == '__main__':
#     unittest.main()
