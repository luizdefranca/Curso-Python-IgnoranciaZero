#!/Anaconda3/python
# -*- coding: UTF-8 -*-

# CGI modules imports
import cgitb

# Import path link to make connections to all folders
import path_link

# Import sql manager and session manager
import MySQLManager

# Traceback for error messages
import traceback

import table_body
import table_navigation

__author__ = 'pedro'


# Enable cgi traceback
cgitb.enable()


def main(form, session):
    # Set the database connector
    db_connector = MySQLManager.MySQLManager

    # We set a create the database manager object
    connector = db_connector("127.0.0.1", "root", "", "iz")

    # We set the panel title for the page
    panel_title = "Log de Acesso"

    # Boolean that informs if we should have an edit columns
    edit = False

    # First we check to see if a post was made
    if "i" in form and form['i']:
        page = int(form['i'])

    # We get the number of rows per page
    rows = 10

    try:
        # We create an array for the fields we wanna retrive
        columns_names = connector.query_columns_names("log")

        # Now we must fill the table. We are going to select 10 rows for
        # each page. To do that we must query for information
        table_info = connector.query_select("log", "*", where=None, order="log_id", desc=True)
    except:
        # If it failed we show the exception
        print(connector.query)
        raise Exception(traceback.format_exc())
    else:
        columns_titles = (
            "Log ID", "Data", "Evento",
            "Usuário", "IP"
        )

        # For the columns that we store an id we must get the
        # column value in the others table. We are going to store
        # the values on the set bellow of variables
        dictionary = {}

        # We set the number of rows necessery
        max = len(table_info)
        pages = round(max / rows)

        # With the table info we create the table
        if page*rows < max:
            limit = page*rows
        else:
            limit = max

        # We also include the table navigation
        html = table_body.main(panel_title, columns_titles, columns_names, page, rows, limit, dictionary, edit, table_info, "")

        # We also include the table navigation
        html += table_navigation.main(pages, page, "log_acessos")

        return html
