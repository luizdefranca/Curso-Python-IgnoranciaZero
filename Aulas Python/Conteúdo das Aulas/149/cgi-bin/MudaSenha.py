#!/Anaconda3/python
# -*- coding: UTF-8 -*-

# CGI modules imports
import cgi
import cgitb

# Import path link to make connections to all folders
import path_link

# Import the form functions
import form_functions

# Import sql manager and session manager
import MySQLManager
import SessionManager

# Traceback for error messages
import traceback
import os
import datetime

__author__ = 'pedro'

# Enable cgi traceback
cgitb.enable()

# Set the database connector
db_connector = MySQLManager.MySQLManager


class MudaSenha(object):
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
        # We save the values gotten
        self.session.set("mudar_senha_senha", form["cSenha1"])
        self.session.set("mudar_senha_confsenha", form["cSenha2"])

        # First we check to see if the passwords are the same
        if form["cSenha1"] == form["cSenha2"]:

            # We set a create the database manager object
            connector = db_connector("127.0.0.1", "root", "", "iz")

            try:
                # Then we try to do the query
                connector.query_update("usuario", ("usuario_senha",), (form['cSenha1'],),
                                       (("usuario_id", "=", self.session.get("usuario")["usuario_id"], ""),))
            except:
                # If it failed we show the exception
                self.session.set("mudar_senha_state", "Erro")
                self.session.set("mudar_senha_message", traceback.format_exc())
            else:
                # Insert the query for the log
                try:
                    connector.query_insert("log", ("log_data", "log_evento", "log_usuario", "log_ip"),
                                           (datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d'), "Mudou a Senha",
                                            self.session.get("usuario")['usuario_login'], os.environ["REMOTE_ADDR"]))
                except:
                    raise Exception(traceback.format_exc())
                else:
                    self.session.set("mudar_senha_state", "Sucesso")
                    self.session.set("mudar_senha_message", "A Senha foi alterada com Sucesso")
        else:
            self.session.set("mudar_senha_state", "Erro")
            self.session.set("mudar_senha_message", "As senhas não são iguais")

        print("Location: ../fetch_page.py?page=mudar_senha\r\n\r")
        self.session.save()

if __name__ == '__main__':
    form = form_functions.form(cgi.FieldStorage())
    print("Content-type: text/html")
    l = MudaSenha()
    l.post(form)


