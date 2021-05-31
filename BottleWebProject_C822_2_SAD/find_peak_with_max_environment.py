from random import randint
from graph import Graph
import GraphNode
import numpy as np

def find_peak_with_max_environment(matrix : Graph, peak_count, level_count):
    #level_count=int(input("введите число ярусов: "))
    ones_matrix=np.eye(peak_count) #вводится число вершин
    one_bool=np.array(ones_matrix, dtype=bool)
    #сделали единичную матрицу как булеву
    total_bool_matrix=[]
    #общая булева матрица
    for i in range(0, level_count):
        matrix=np.array(matrix)
        if i==0:
            matrix_bool=np.array(matrix, dtype=bool)
            total_bool_matrix.append(matrix_bool)
        else:
            matrix_new=np.linalg.matrix_power(matrix, i+1)
            matrix_new=np.array(matrix_new, dtype=bool)
            total_bool_matrix.append(matrix_new)

    answer_matrix=one_bool
    for i in range(0, level_count):
        answer_matrix=answer_matrix+total_bool_matrix[i]
    answer_matrix=np.array(answer_matrix, dtype=int)
    list_with_env=np.sum(answer_matrix, axis=1)
    max_elem=list_with_env[0]
    point_with_max_environment=[]
    for item in list_with_env:
        if item>max_elem:
            max_elem=item
    for i in range(0, len(list_with_env)):
        if list_with_env[i]==max_elem:
            point_with_max_environment.append(i+1)       
    print(answer_matrix)
    print("Вершины с максимальным окружением: " + str(point_with_max_environment))

test_matrix = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
g=Graph(test_matrix)
find_peak_with_max_environment(g.matrix,len(g.nodes), 3)