#!/Anaconda3/python
# -*- coding: UTF-8 -*-


__author__ = 'pedro'


def main(form, session):
    html = """
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta content="text/html; charset=UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
        <title>Ignorância Zero</title>

        <!-- Bootstrap -->
        <link href="includes/css/bootstrap.min.css" rel="stylesheet">
        <link href="includes/css/bootstrap-glyphicons.css" rel="stylesheet">
        <link href="css/styles.css" rel="stylesheet">

        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
            <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->

        <script src="includes/js/modernizr-2.6.2.min.js"></script>
    </head>

    <body>
        <div class="nav navbar-default navbar-fixed-top">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#myNavbar" aria-expanded="false">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>

                    <a class="navbar-brand" href="fetch_page.py?page=inicial">Ignorância Zero</a>
                </div>

                <div class="collapse navbar-collapse" id="myNavbar">
                    <ul class="nav navbar-nav pull-left">
                        <li class='"""
    html += "active'" if form["page"] == "inicial" else ""
    html += """'>
                            <a href="fetch_page.py?page=inicial">Inicial</a>
                        </li>

                        <li class="dropdown">
                            <a class="dropdown-toggle" data-toggle="dropdown">Gerenciar<strong class="caret"></strong></a>

                            <ul class="dropdown-menu">
                                <li class="dropdown-header">Arquivos</li>
                                <li><a href="fetch_page.py?page=menu">Executar Scripts</a></li>
                                <li><a href="fetch_page.py?page=download">Download</a></li>
                                <li><a href="fetch_page.py?page=upload">Upload</a></li>
                            </ul>
                        </li>"""

    if session.get("usuario")["usuario_nivel"] == 1:
        html += """
                        <li class="dropdown">
                            <a class="dropdown-toggle" data-toggle="dropdown">Administração<strong class="caret"></strong></a>

                            <ul class="dropdown-menu">
                                <li><a href="fetch_page.py?page=log_acessos&i=1">Log de Acessos</a></li>
                            </ul>
                        </li>
        """

    html += """
                        <li class='"""
    html += "active'" if form["page"] == "sobre" else ""
    html += """'>
                            <a href="fetch_page.py?page=sobre">Sobre</a>
                        </li>
                    </ul>

                    <ul class="nav navbar-nav pull-right">
                        <li class="dropdown">
                            <a class="dropdown-toggle" data-toggle="dropdown">
                                <span class="glyphicon glyphicon-user"></span>Minha Conta<strong class="caret"></strong>
                            </a>

                            <ul class="dropdown-menu">
                                <li class="dropdown-header">Bem-Vindo """
    html += session.get("usuario")["usuario_login"] + """</li>
                                <li><a href="fetch_page.py?page=mudar_senha"><span class="glyphicon glyphicon-wrench"></span>Alterar Senha</a></li>
                                <li><a href="#"><span class="glyphicon glyphicon-refresh"></span>Alterar Perfil</a></li>
                                <li class="divider"></li>
                                <li><a href="cgi-bin/Sair.py"><span class="glyphicon glyphicon-off"></span>Sair</a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="container" id="main">
    """

    return html