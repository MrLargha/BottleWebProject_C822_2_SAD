from unittest import TestCase
from subgraph_finder import ClickFinder
from graph import Graph


class TestClickFinder(TestCase):

    """Unittest data"""
    big_graph = Graph([[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
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

    def test_find_clicks(self):
        finder = ClickFinder(self.big_graph)
        result = finder.find_clicks()
        self.assertTrue(len(result) == 5)
        self.assertTrue(result[0] == self.big_graph.nodes[0:5])
        # TODO: Implement other equations

    def test_save_result_to_file(self):
        finder = ClickFinder(self.big_graph)
        finder.find_clicks()
        path = finder.save_result_to_file()
        try:
            f = open(path, 'r')
            return
        except Exception:
            self.fail("File is not saved correctly")