#!/Anaconda3/python
# -*- coding: UTF-8 -*-

# CGI modules imports
import cgi
import cgitb
import sys

sys.path.append("classes")
sys.path.append("functions")
sys.path.append("template")
sys.path.append("pages")
sys.path.append("cgi-bin")

# Import the functions
import char_functions
import form_functions

# Import the session manager
import SessionManager

# Import the template pages
import head
import footer

__author__ = 'pedro'

# Enable cgi traceback
cgitb.enable()

# Create the session object
session = SessionManager.SessionManager()

# Check if user is set
if not session.isset("usuario"):
    print('Content-type: text/html')
    print("Location: login.py\r\n\r")

# Get the form
form = form_functions.form(cgi.FieldStorage())

# Print the beginning of the page
print('Content-type: text/html\n')

# Print the page body
if form["page"] != "upload":
    session.set("upload_status", "")
    session.save()
if form["page"] != "mudar_senha":
    session.set("mudar_senha_state", "")
    session.set("mudar_senha_message", "")
    session.set("mudar_senha_senha", "")
    session.set("mudar_senha_confsenha", "")
    session.save()

# Print the page header
print(head.main(form, session))

body = __import__(form["page"])
print(body.main(form, session))

# Print the page foot
print(footer.main(form, session))
