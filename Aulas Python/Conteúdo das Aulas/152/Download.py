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

class Download(object):
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
        # The value of the form
        i = int(form["cArq"])

        # Get the file
        arq = os.path.join("..", "data", self.session.get("usuario")["usuario_login"], self.session.get("arquivos")[i])

        # HTTP Header
        print("Content-Type:application/octet-stream; name=\"%s\"" % self.session.get("arquivos")[i])
        print("Content-Disposition: attachment; filename=\"%s\"" % self.session.get("arquivos")[i])
        print()

        # Actual File Content will go hear.
        fo = open(arq, "r")
        string = fo.read()
        print(string)

        # Close opend file
        fo.close()

        # Insert the query for the log
        try:
            # We set a create the database manager object
            connector = db_connector("127.0.0.1", "root", "", "iz")

            connector.query_insert("log", ("log_data", "log_evento", "log_usuario", "log_ip"),
                                   (datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d'), "Fez Download de " + self.session.get("arquivos")[i],
                                    self.session.get("usuario")['usuario_login'], os.environ["REMOTE_ADDR"]))
        except:
            raise Exception(traceback.format_exc())

if __name__ == '__main__':
    form = form_functions.form(cgi.FieldStorage())
    l = Download()
    l.post(form)
