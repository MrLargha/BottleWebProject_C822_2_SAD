from datetime import datetime

from bottle import route, template
from graph import Graph


@route('/render')
def render_graph():
    big_graph = Graph([[1, 0, 1, 0],
                       [1, 1, 1, 1],
                       [1, 1, 1, 1],
                       [1, 1, 1, 1]])
    return template('graph_view', title='Отображение графа',
                    year=datetime.now().year, image_path=big_graph.save_to_file())
