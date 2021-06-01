from graph import Graph
import GraphNode
from datetime import datetime
import numpy as np
from bottle import route, post, template, request
import request_utils


@post('/find_peak_with_max_environment', method='post')
#метод решения поставленной задачи
def find_peak_with_max_env():
    matrix = request_utils.extract_matrix_from_request_params(request.forms)#полчение матрицы со страницы
    g=Graph(matrix)
    for i in range(0, len(g.nodes)):
        g.nodes[i].name=i+1
    level_count = int(request.forms.get("sergey_yarus"))#полчения числа ярусов
    peak_count=len(g.nodes)#получение числа вершин
    ones_matrix=np.eye(peak_count) #создание единичной матрицы

    """Сделать страницы с выводом ошибки!"""
    one_bool=np.array(ones_matrix, dtype=bool)#преобразование ее в булеву матрицу для дальнейших операций
    total_bool_matrix=[]    #общая булева матрица
    for i in range(0, level_count): #цикл для создания булевых матриц, необходимых для нахождения матрицы достижимости
        matrix=np.array(matrix)
        if i==0:
            matrix_bool=np.array(matrix, dtype=bool)
            total_bool_matrix.append(matrix_bool)
        else:
            matrix_new=np.linalg.matrix_power(matrix, i+1)
            matrix_new=np.array(matrix_new, dtype=bool)
            total_bool_matrix.append(matrix_new)

    answer_matrix=one_bool#создание матрицы достижимости
    #цикл для получения матрицы достижимости
    for i in range(0, level_count):
        answer_matrix=answer_matrix+total_bool_matrix[i]
    answer_matrix=np.array(answer_matrix, dtype=int) #перевод матрицы из булева представления в числовое (0 и 1)
    #объявление переменных необходимых для нахождения вершин с максимальным окржуением
    list_with_env=np.sum(answer_matrix, axis=1)
    max_elem=list_with_env[0]
    #массив вершин с максимальным окружением
    point_with_max_environment=[]
    for item in list_with_env:
        if item>max_elem:
            max_elem=item
    for i in range(0, len(list_with_env)):
        if list_with_env[i]==max_elem:
            point_with_max_environment.append(i+1)       
    path = g.save_to_file(size=30)
    result_peak=str(point_with_max_environment)
    result_peak=result_peak[1:-1]
    return template('graph_encirclement_view', title='Результат поиска вершин с максимальным окружением', peak_count=result_peak,
                    image_path=path, year=datetime.now().year)


@post('/graph_encirclement', method='post')
def search():
    matrix_dim = int(request.forms.get("MATRIX"))
    level_count = int(request.forms.get("LEVEL"))
    return template('enter_matrix', title='Поиск вершин с максимальным окружением',
                    message='Задача Сергея Пластовца на поиск вершин с максимальным окружением',
                    year=datetime.now().year, rows=matrix_dim, columns=matrix_dim,
                    names=Graph.get_nodes_names(matrix_dim),
                    callback='find_peak_with_max_environment',
                    yarus=level_count)









"""
%import find_peak_with_max_environment
%from graph import Graph
%import GraphNode

%test_matrix = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
%[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
%[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
%[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
%[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
%[0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
%[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
%[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
%[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
%[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
%[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
%[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
%[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
%[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
%[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
%[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
%[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
%g=Graph(test_matrix)
%answ_matrix, max_peak=find_peak_with_max_environment.find_peak_with_max_env(g.matrix,len(g.nodes), 3)
%image_path=g.save_to_file()
<img src="{{image_path}}" />
<h3>{{ answ_matrix }}</h3>
<h3>{{ max_peak }}</h3>

"""