from datetime import datetime
from bottle import post, template, request
import request_utils
from graph import Graph
from euler_path_search import find_euler_path
from task_logger import Logger


@post('/eulerian_path', method='post')
def search():
    try:
        matrix_dim = int(request.forms.get("MATRIX"))
    except:
        return template("error", message='Количество вершин не введено!')

    return template('enter_matrix', title='Поиск Эйлерового пути в графе',
                    message='Задача Дмитрия Повеличенко на поиск Эйлерового пути в графе',
                    year=datetime.now().year, rows=matrix_dim, columns=matrix_dim,
                    names=Graph.get_nodes_names(matrix_dim),
                    callback='euler_graph_entered',
                    yarus=-1)


@post("/euler_graph_entered", method="post")
def enter_graph():
    matrix = request_utils.extract_matrix_from_request_params(request.forms)
    g = Graph(matrix)
    res = find_euler_path(g)
    path = ""

    logger = Logger('euler_path_search.log')
    log_msg = "Entered matrix: \n" + str(matrix).replace('[', '').replace(']', '')

    if type(res) == list:
        msg = " -> ".join(map(lambda i: g.nodes[i].name, res))
        logger.push_log(log_msg + "\nEuler path: " + msg)
        g = Graph.create_from_path(res)
        path = g.save_to_file(500)
    else:
        msg = res
        logger.push_log(log_msg + "\n" + msg)

    return template('euler_path_view', title='Результат поиска ', message=msg,
                    image_path=path)
