import unittest
import graph
import numpy as np
from find_peak_with_max_environment import find_reachability_matrix
default_matrix = [[0, 1, 0, 0, 0 ],[1, 0, 1, 0, 0],[0, 1, 0, 1, 1 ],[0, 0, 1, 0, 1 ],[0, 0, 1, 1, 0]]
result_matrix_for_level2= [[1,1,1,0,0,],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1]]
 # сдеать тест показывающий разницу в зависимоти от введенного яруса
class Test_test_graph_encirclement(unittest.TestCase):
    def test_level_count_2(self):
        answer_matrix= find_reachability_matrix(5,2,default_matrix)
        self.assertTrue((np.array(result_matrix_for_level2==answer_matrix).all()))
    def test_level_count_3(self):
        answer_matrix= find_reachability_matrix(5,3,default_matrix)
        self.assertFalse((np.array(result_matrix_for_level2==answer_matrix).all()))
if __name__ == '__main__':
    unittest.main()
