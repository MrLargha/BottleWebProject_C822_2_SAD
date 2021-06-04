"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )


@route('/euler')
@view('eulerian_path')
def euler():
    return dict(
        title='Эйлеров путь',
        message='Задача Дмитрия Повеличенко на поиск Эйлерова пути',
        year=datetime.now().year
    )


@route('/subgraph')
@view('subgraph_search')
def subgraph():
    return dict(
        title='Поиск полных подграфов',
        message='Задача на поиск полных подграфов из 5 вершин в графе',
        year=datetime.now().year
    )


@route('/encirclement')
@view('graph_encirclement')
def circle():
    return dict(
        title='Наибольшее окружение',
        message='Задача на поиск вершин графа с наибольшим окружением',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='Об авторах',
        message='Пару слов об авторах этого чудеснейшего сайта',
        year=datetime.now().year
    )
