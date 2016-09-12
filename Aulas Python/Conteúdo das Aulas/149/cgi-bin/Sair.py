#!/Anaconda3/python
# -*- coding: UTF-8 -*-

# CGI modules imports
import cgitb

# Import path link to make connections to all folders
import path_link

# Import sql manager and session manager
import SessionManager

__author__ = 'pedro'

# Enable cgi traceback
cgitb.enable()

print("Content-type: text/html")

# Get the current session
session = SessionManager.SessionManager()

# Destroy the session
session.destroy()

# Redirect to the login page
print("Location: ../login.py\r\n\r")
