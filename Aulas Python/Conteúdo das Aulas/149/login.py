#!/Anaconda3/python
# -*- coding: UTF-8 -*-

# CGI modules imports
import cgitb

# Import path link to make connections to all folders
import sys

sys.path.append("classes")
sys.path.append("functions")
sys.path.append("template")
sys.path.append("pages")
sys.path.append("cgi-bin")

# Import session manager
import SessionManager
from char_functions import enc_print

# Enable cgi traceback
cgitb.enable()

# Create the session manager
session = SessionManager.SessionManager(login_menu="login", login_message="Digite o usuário e a senha")

# We check to see if the user is set
if session.isset("usuario"):
    print("Content-type: text/html")
    print("Location: ../fetch_page.py?page=inicial\r\n\r")

else:
    # Check if the session is not set
    if not session.isset("login_menu"):
        session.set("login_menu", "login")
        session.set("login_message", "Digite o usuário e a senha")
        session.save()

    # We enc_print the beginning of the page
    enc_print("Content-type: text/html")

    enc_print("")

    # Set the beginning of the session page
    html = """
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="Minha pagina Inicial" content="">
        <meta name="Pedro" content="">

        <title>Login</title>

        <!-- Bootstrap -->
        <link href="includes/css/bootstrap.min.css" rel="stylesheet">
        <link href="css/login.css" rel="stylesheet">

        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
            <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
    </head>
    <body>
        <div class="container">
            <div class="card card-container">
                <h3 class="text-center" id="pageTitle"> Ignorância Zero </h3>
                <img class="logo-img-card" id="logo-img" src="http://bootsnipp.com/img/logo.jpg">

                <div id="div-forms">
"""

    if session.get('login_menu') == 'login':
        # If we ware at the login menu we add to the html
        html += """
                    <div id="login-form">
                        <form class="form-signin" method="post" action="cgi-bin/Login.py">
                                <div id="div-login-msg">
                                    <div id="icon-login-msg" class="glyphicon glyphicon-chevron-right"></div>
                                    <span id="text-login-msg">"""+session.get("login_message") + """</span>
                                </div>
        """
    else:
        # Otherwise we add the menu hidden
        html += """
                    <div id="login-form" hidden>
                        <form class="form-signin" method="post" action="cgi-bin/Login.py">
                            <div id="div-login-msg">
                                <div id="icon-login-msg" class="glyphicon glyphicon-chevron-right"></div>
                                <span id="text-login-msg">Digite o usuário e a senha</span>
                            </div>
        """

    # We add the rest of the login menu
    html += """
                            <input type="text" id="tUser" name="cUser" class="form-control" placeholder="Usuário" required autofocus>
                            <input type="password" id="tPassword" name="cSenha" class="form-control" placeholder="Senha" required>
                            <div id="remember" class="checkbox">
                                <label>
                                    <input type="checkbox" value="remember-me"> Lembre-me
                                </label>
                            </div>
                            <button name="bLogin" class="btn btn-lg btn-primary btn-block btn-signin" type="submit" value="submit">Entrar</button>
                        </form><!-- /form -->
                        <a id="login_lost_btn" href="#" class="forgot-password">
                            Esqueceu a senha?
                        </a>
                        <a id="login_register_btn" href="#" class="forgot-password">
                            Registrar
                        </a>
                    </div>
    """

    # We do se same operation to the register menu
    if session.get('login_menu') == 'register':
        # If we ware at the login menu we add to the html
        html += """
                    <div id="register-form">
                        <form class="form-signin" method="post" action="cgi-bin/Login.py">
                                <div id="div-login-msg">
                                    <div id="icon-login-msg" class="glyphicon glyphicon-chevron-right"></div>
                                    <span id="text-login-msg">"""+session.get("login_message") + """</span>
                                </div>
        """
    else:
        # Otherwise we add the menu hidden
        html += """
                    <div id="register-form" hidden>
                        <form class="form-signin" method="post" action="cgi-bin/Login.py">
                            <div id="div-login-msg">
                                <div id="icon-login-msg" class="glyphicon glyphicon-chevron-right"></div>
                                <span id="text-login-msg">Preencha os campos para Registrar-se</span>
                            </div>
        """

    html += """
                            <input type="text" id="tNome" name="cNome" class="form-control" placeholder="Digite seu Nome" required>
                            <input type="email" id="tMail" name="cMail" class="form-control" placeholder="Digite seu email" required>
                            <input type="text" id="tUser" name="cUser" class="form-control" placeholder="Usuário" required>
                            <input type="password" id="tPassword1" name="cSenha1" class="form-control" placeholder="Senha" required>
                            <input type="password" id="tPassword2" name="cSenha2" class="form-control" placeholder="Confirme a Senha" required>

                            <button name="bRegister" class="btn btn-lg btn-primary btn-block btn-signin" type="submit" value="submit">Registrar</button>
                        </form><!-- /form -->
                        <a href="#" id="register_login_btn" class="forgot-password">
                            Login
                        </a>
                        <a href="#" id="register_lost_btn" class="forgot-password">
                            Esqueceu a senha?
                        </a>
                    </div>
    """

    # We do se same operation to the lost menu
    if session.get('login_menu') == 'lost':
        # If we ware at the login menu we add to the html
        html += """
                    <div id="lost-form">
                        <form class="form-signin" method="post" action="cgi-bin/Login.py">
                                <div id="div-login-msg">
                                    <div id="icon-login-msg" class="glyphicon glyphicon-chevron-right"></div>
                                    <span id="text-login-msg">"""+session.get("login_message") + """</span>
                                </div>
        """
    else:
        # Otherwise we add the menu hidden
        html += """
                    <div id="lost-form" hidden>
                        <form class="form-signin" method="post" action="cgi-bin/Login.py">
                            <div id="div-login-msg">
                                <div id="icon-login-msg" class="glyphicon glyphicon-chevron-right"></div>
                                <span id="text-login-msg">Digite o seu email e mandaremos sua senha</span>
                            </div>
        """

    # We add the rest of the html
    html += """
                            <input type="email" id="tMail" name="cMail" class="form-control" placeholder="Digite seu email" required>

                            <button name="bLost" class="btn btn-lg btn-primary btn-block btn-signin" type="submit" value="submit">Enviar</button>
                        </form><!-- /form -->
                        <a href="#" id="lost_login_btn" class="forgot-password">
                            Login
                        </a>
                        <a href="#" id="lost_register_btn" class="forgot-password">
                            Registrar
                        </a>
                    </div>
                </div>

            </div><!-- /card-container -->
        </div><!-- /container -->

        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="includes/js/jquery-1.12.0.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="includes/js/bootstrap.min.js"></script>

        <script src="js/login.js"></script>
    </body>
</html>
    """

    # And we enc_print the hole page
    enc_print(html)
