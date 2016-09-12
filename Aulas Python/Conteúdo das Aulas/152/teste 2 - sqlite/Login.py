#!/Users/pedro/Anaconda3/python
# -*- coding: UTF-8 -*-

# CGI modules imports
import cgi
import cgitb

# Import the form functions
import form_functions

# Import sql manager
# import MySQLManager
import SQLiteManager

# Traceback for error messages
import traceback
import os
import datetime

__author__ = 'pedro'

# Enable cgi traceback
cgitb.enable()

# Set the database connector
# db_connector = MySQLManager.MySQLManager
db_connector = SQLiteManager.SQLiteManager


class Login(object):
    """
    Handle the login operations and redirects
    """
    def __init__(self):
        """
        Creates the login object handler
        :return:
        """
        # Set the html to be empty
        self.html = ""

    def post(self, form):
        """
        Receive the values from form
        :param form: dictionary with post values
        :return:
        """
        # First we check if the user is trying to login
        if "bLogin" in form:
            self.login(form)
        elif "bRegister" in form:
            self.register(form)

    def login(self, form):
        """
        Execute the login operations
        :param form:
        :return:
        """
        # We set a create the database manager object
        connector = db_connector("127.0.0.1", "root", "", "iz")

        try:
            # Then we try to do the query
            result = connector.query_select("usuario", "*",
                                            where=(("usuario_login", "=", form["cUser"], "AND"),
                                                   ("usuario_senha", "=", form["cSenha"], ""))
                                            )
        except:
            # If it failed we show the exception
            raise Exception(traceback.format_exc())
        else:
            # If it works we check to see if a user was correctly selected
            if len(result) > 0:
                # Insert the query for the log
                try:
                    connector.query_insert("log", ("log_data", "log_evento", "log_usuario", "log_ip"),
                                           (datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d'), "Entrou",
                                            form["cUser"], os.environ["REMOTE_ADDR"]))
                except:
                    raise Exception(traceback.format_exc())
                else:
                    self.redirect_to_inicial(result)
            # If it was not we
            else:
                # Redirect to the login page showing the correct error message
                self.redirect_to_login()

    def register(self, form):
        """
        Register a new user
        :param form:
        :return:
        """
        if form["cSenha1"] != form["cSenha2"]:
            self.redirect_to_register("As senhas não são iguais")
        else:
            # We set a create the database manager object
            connector = db_connector("127.0.0.1", "root", "", "iz")

            try:
                # We check to see if there is no user with that name
                result = connector.query_select("usuario", "*", where=(("usuario_login", "=", form["cUser"], ""),))
                if len(result) > 0:
                    self.redirect_to_register("O Usuário " + form["cUser"] + " já foi cadastrado")
                    return

                # We check to see if there is no user with that mail
                result = connector.query_select("usuario", "*", where=(("usuario_email", "=", form["cMail"], ""),))
                if len(result) > 0:
                    self.redirect_to_register("O Email " + form["cMail"] + " já foi cadastrado")
                    return

                # Then we try to do the query
                connector.query_insert("usuario", ("usuario_login", "usuario_senha", "usuario_nome", "usuario_email", "usuario_nivel"),
                                       (form["cUser"], form['cSenha1'], form["cNome"], form["cMail"], 2))
            except:
                # If it failed we show the exception
                raise Exception(traceback.format_exc())
            else:
                # Insert the query for the log
                try:
                    connector.query_insert("log", ("log_data", "log_evento", "log_usuario", "log_ip"),
                                           (datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d'), "Registrou-se",
                                            form["cUser"], os.environ["REMOTE_ADDR"]))
                except:
                    raise Exception(traceback.format_exc())
                else:
                    # Then we try to login with the new user
                    form["cSenha"] = form["cSenha1"]
                    self.login(form)

    def redirect_to_login(self):
        """
        Redirect to the login page with login menu
        """
        print()
        print("<html><head>")
        print("")
        print("</head><body>")
        print("Usuário ou senha incorretos!!!!")
        print("</body></html>")

    def redirect_to_register(self, message):
        """
        Redirect to the login page with login menu
        """
        print()
        print("<html><head>")
        print("")
        print("</head><body>")
        print(message)
        print("</body></html>")

    def redirect_to_inicial(self, result):
        """
        Redirect to the menu page of the iz website
        :return:
        """
        print()
        print("<html><head>")
        print("")
        print("</head><body>")
        print("Login Realizado com Sucesso!!!!")
        print("</body></html>")

if __name__ == '__main__':
    form = form_functions.form(cgi.FieldStorage())
    print("Content-type: text/html")
    l = Login()
    l.post(form)

