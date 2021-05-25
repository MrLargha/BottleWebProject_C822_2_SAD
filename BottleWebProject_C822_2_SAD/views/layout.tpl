<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - математическое моделирование</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body>
    <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="/" class="navbar-brand">Математическое моделирование</a>
            </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li><a href="/home">Домашняя</a></li>
                    <li><a href="/euler">Эйлеров цикл</a></li>
                    <li><a href="/subgraph">Поиск подграфов</a></li>
                    <li><a href="/encirclement">Поиск вершин с наибольшим окружением</a></li>
                    <li><a href="/about">Об авторах</a></li>
                </ul>
            </div>
        </div>
    </div>

    <div class="container body-content">
        {{!base}}
        <hr />
        <footer>
            <p>&copy; {{ year }} - Математическое моделирование, С822, Богданов-Пластовец-Повеличенко</p>
        </footer>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>
