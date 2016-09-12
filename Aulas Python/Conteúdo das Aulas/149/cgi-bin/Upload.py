#!c:/Anaconda3/python
# coding: UTF-8

# CGI modules imports
import cgi
import cgitb

# Import path link to make connections to all folders
import path_link

# Import sql manager and session manager
import MySQLManager
import SessionManager

# Traceback for error messages
import os
import traceback
import datetime

__author__ = 'pedro'

# Enable cgi traceback
cgitb.enable()

# Set the database connector
db_connector = MySQLManager.MySQLManager


class Upload(object):
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
        # Get filename here.
        fileitem = form['cFile']

        # Path to the user file folder
        user_path = os.path.join("..", "data", self.session.get("usuario")["usuario_login"])

        # Verify if a file gas been selected
        if fileitem.filename:
            # Check if directory has been created
            if not os.path.exists(user_path):
                # Create directory
                os.mkdir(user_path)

            # Remove client directory path
            fn = os.path.basename(fileitem.filename)

            # Write file on server
            open(os.path.join(user_path, fn), 'wb').write(fileitem.file.read())

            # Criamos a mensagem a ser disponibilizada
            self.session.set("upload_status", "Sucesso")
            self.session.set("upload_message", "Upload bem sucedido")
            print("Location: ../fetch_page.py?page=upload\r\n\r")
            self.session.save()

            # Insert the query for the log
            try:
                # We set a create the database manager object
                connector = db_connector("127.0.0.1", "root", "", "iz")

                connector.query_insert("log", ("log_data", "log_evento", "log_usuario", "log_ip"),
                                       (datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d'), "Fez Upload de " + fn,
                                        self.session.get("usuario")['usuario_login'], os.environ["REMOTE_ADDR"]))
            except:
                raise Exception(traceback.format_exc())

        else:
            self.session.set("upload_status", "Fracasso")
            self.session.set("upload_message", str(fileitem.filename))
            print("Location: ../fetch_page.py?page=upload\r\n\r")
            self.session.save()

if __name__ == '__main__':
    form = cgi.FieldStorage()
    l = Upload()
    print("Content-Type: text/html")
    l.post(form)
