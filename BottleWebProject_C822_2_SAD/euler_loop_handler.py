from datetime import datetime
from bottle import post, template, request
import request_utils
from graph import Graph
from euler_loop_search import find_euler_loop


@post('/eulerian_loop', method='post')
def search():
    try:
        matrix_dim = int(request.forms.get("MATRIX"))
    except:
        return template("error", message='Количество вершин не введено!')

    if matrix_dim < 1:
        return template("error", message='Вершин должно быть не меньше одной!')

    return template('enter_matrix', title='Поиск эйлерового цикла в графе',
                    message='Задача Дмитрия Повеличенко на поиск эйлерового цикла в графе',
                    year=datetime.now().year, rows=matrix_dim, columns=matrix_dim,
                    names=Graph.get_nodes_names(matrix_dim),
                    callback='euler_graph_entered',
                    yarus=-1)


@post("/euler_graph_entered", method="post")
def enter_graph():
    matrix = request_utils.extract_matrix_from_request_params(request.forms)
    g = Graph(matrix)
    res = find_euler_loop(g)
    path = ""

    if type(res) == list:
        msg = " -> ".join(map(lambda i: g.nodes[i].name, res))
        g = Graph.create_from_path(res)
        path = g.save_to_file(500)
    else:
        msg = res

    return template('euler_loop_view', title='Результат поиска ', message=msg,
                    image_path=path)
