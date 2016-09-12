#!/Users/pedro/Anaconda3/python
# -*- coding: UTF-8 -*-

# CGI modules imports
import cgi
import cgitb

# Import path link to make connections to all folders
import path_link

# Import the form functions
import form_functions

# Import sql manager and session manager
# import MySQLManager
import SQLiteManager
import SessionManager

# Traceback for error messages
import os
import traceback
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

        # Open the session manager
        self.session = SessionManager.SessionManager()

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
                    # We create a new folder inside data
                    os.mkdir(os.path.join("..", "data", form["cUser"]))

                    # Then we try to login with the new user
                    form["cSenha"] = form["cSenha1"]
                    self.login(form)

    def redirect_to_login(self):
        """
        Redirect to the login page with login menu
        """
        self.session.set('login_menu', "login")
        self.session.set('login_message', "Usuário ou senha incorretos")
        print("Location: ../login.py\r\n\r")
        self.session.save()

    def redirect_to_register(self, message):
        """
        Redirect to the login page with login menu
        """
        self.session.set('login_menu', "register")
        self.session.set('login_message', message)
        print("Location: ../login.py\r\n\r")
        self.session.save()

    def redirect_to_inicial(self, result):
        """
        Redirect to the menu page of the iz website
        :return:
        """
        self.session.unset('login_menu')
        self.session.unset('login_message')
        self.session.set("usuario", result[0])

        # We also get all the script the user has
        try:
            path = os.path.join("..", "data", self.session.get("usuario")['usuario_login'])
            l = os.listdir(path)
        except:
            path = os.path.join("data", self.session.get("usuario")['usuario_login'])
            l = os.listdir(path)
        l.sort()
        for s in l.copy():
            p = os.path.join(path, s)
            if not os.path.isfile(p):
                l.remove(p)
        self.session.set("arquivos", l)

        # Then we redirect
        print("Location: ../fetch_page.py?page=inicial\r\n\r")
        self.session.save()

if __name__ == '__main__':
    form = form_functions.form(cgi.FieldStorage())
    print("Content-type: text/html")
    l = Login()
    l.post(form)

