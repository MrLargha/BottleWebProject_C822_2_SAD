% rebase('layout.tpl', title='Домашняя страница', year=year)

<div class="jumbotron" style="border-radius: 15px;" >
    <h1>Математическое моделирование</h1>
    <p class="lead">Потрясающий сайт про математическое моделирование. Выполнен на УП 02. Содержит решения трёх задача</p>
    <p><a href="/about" class="btn btn-primary btn-large">Узнать об авторах</a></p>
</div>

<div class="row">
    <div class="col-md-4">
        <h2>Эйлеров цикл</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
        <p><a class="btn btn-default" href="/euler">Перейти &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Поиск подграфа</h2>
        <p>Страница о поиске полного подграфа из 5 вершин в другом графе. Для поиска используется алгоритм Брона-Кербоша. Есть возможность задать свой граф в виде матрицы смежности и визуализировать результат</p>
        <p><a class="btn btn-default" href="/subgraph">Перейти &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Поиск вершин с наибольшим окружением</h2>
        <p>Страница о поиске вершин с максимальным окружением. Для поиска используется матрица достижимости, а в качестве входных параметров выступает матрица смежности и число ярусов графа</p>
        <p><a class="btn btn-default" href="/enciclement">Перейти &raquo;</a></p>
    </div>
</div>
