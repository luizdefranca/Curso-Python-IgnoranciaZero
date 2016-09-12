#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

print('Content-type: text/html\n')

# Imprime a head da página
print(open("html/head.html").read())

# Começa a imprimir o corpo da página
print("<body>")

# Imprime a barra de navegação
print(open("html/navbar.html").read())

# Imprimimos a página que desejamos a partir do que foi
# passado no form
print(open("html/%s.html" % form['page'].value).read())

# Imprimimos a parte de baixo da página
print(open("html/feet.html").read())

