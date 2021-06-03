from graph import Graph
import GraphNode
from datetime import datetime
import numpy as np
from bottle import route, post, template, request
import request_utils
import task_logger
from task_logger import Logger


@post('/find_peak_with_max_environment', method='post')
#метод решения поставленной задачи
def find_peak_with_max_env():
    matrix = request_utils.extract_matrix_from_request_params(request.forms)#полчение матрицы со страницы
    #участок кода с логгированием
    logger = Logger('graph_encirclement.log')
    logger.push_log("Entered matrix: \n" + str(matrix).replace('[', '').replace(']', ''))
    logger.push_log("Searching peak with max encirclement...")
    g=Graph(matrix)
    for i in range(0, len(g.nodes)):
        g.nodes[i].name=i+1
    level_count = int(request.forms.get("sergey_yarus"))#полчения числа ярусов
    peak_count=len(g.nodes)#получение числа вершин
    answer_matrix=find_reachability_matrix(peak_count, level_count,matrix)
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
    path = g.save_to_file(size_of_node=1500,size=30)
    result_peak=str(point_with_max_environment)
    result_peak=result_peak[1:-1]
    logger.push_log("Reachability matrix: \n" + str(answer_matrix).replace('[', '').replace(']', ''))
    logger.push_log("Peak's with max encirclement: " + str(result_peak))
    return template('graph_encirclement_view', title='Результат поиска вершин с максимальным окружением', peak_count=result_peak,
                    image_path=path, year=datetime.now().year, ach_mtx=answer_matrix)

def find_reachability_matrix(peak_count, level_count, matrix):
    ones_matrix=np.eye(peak_count) #создание единичной матрицы
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
    return answer_matrix

@post('/graph_encirclement', method='post')
def search():
    try:
        matrix_dim = int(request.forms.get("MATRIX"))
        level_count = int(request.forms.get("LEVEL"))
        int_nodes_name=[]
        for i in range(0, matrix_dim):
            int_nodes_name.append(i+1)
        if level_count<0:
            return template('error', message='Число ярусов не может быть меньше 0! Попробуйте еще раз!')
    except ValueError:
        return template('error', message='Введите кол-во вершин в графе!')
    return template('enter_matrix', title='Поиск вершин с максимальным окружением',
                    message='Перед вами матрица смежности вашего графа. Отметьте те клетки, на пересечении которых существует связь',
                    year=datetime.now().year, rows=matrix_dim, columns=matrix_dim,
                    names=int_nodes_name,
                    callback='find_peak_with_max_environment',
                    yarus=level_count)

