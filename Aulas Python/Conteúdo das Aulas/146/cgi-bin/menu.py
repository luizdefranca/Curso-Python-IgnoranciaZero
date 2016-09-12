#!/usr/bin/python

import cgi, sys
import cgitb; cgitb.enable()

from os import listdir
from os.path import isfile, join

form = cgi.FieldStorage()

print("Content-type: text/html")

html = """
<TITLE>Minha Pagina</TITLE>
<H1>Nossos Scripts CGI</H1>
<HR>
<H4> %(nome)s, voce pode executar os seguintes scripts</H4>
"""
path = 'cgi-bin'
l = listdir(join('.', path))
l.sort()
for s in l:
    if isfile(join(path, s)) and 'cgi' in s:
        html += '<p><a href=%s> %s </a></p>\n' % (s, s)
html += '<HR>'

data = {}

for field in ('nome', 'idade'):
    if not field in form:
        data[field] = '(unknown)'
    else:
        if not isinstance(form[field], list):
            data[field] = form[field].value
        else:
            values = [x.value for x in form[field]]
            data[field] = ' e '.join(values)

print(html % data)
