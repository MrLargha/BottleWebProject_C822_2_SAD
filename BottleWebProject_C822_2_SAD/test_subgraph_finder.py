from unittest import TestCase
from graph import Graph
from subgraph_finder import check_full


class Test(TestCase):
    def __init__(self, method_name="runTest"):
        self.full_graph = Graph([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]])
        self.not_full_graph = Graph(
            [[0, 0, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 0, 1], [1, 1, 1, 1, 0]])
        super().__init__(methodName=method_name)

    def test_check_full(self):
        self.assertTrue(check_full(self.full_graph))
        self.assertFalse(check_full(self.not_full_graph))
