#!/usr/bin/python

import cgi, sys
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

print("Content-type: text/html")

html = """
<TITLE>Minha Pagina</TITLE>
<H1>Bem Vindo</H1>
<HR>
<H4> Eae %(time)s de %(cidade)s</H4>
<H4>Seu nome e %(nome)s</H4>
<H4>Sua idade e %(idade)s</H4>
<H4>Voce usa sapatos: %(tamanho)s</H4>
<H4>Sua ideologia e %(politica)s</H4>
<H4>Sua cor de Cabelo e %(cabelo)s</H4>
<H4>Voce tambem disse:</H4>
<P>%(comentario)s</P>
<HR>"""

data = {'time': form['time'].value, 'cidade': form['cidade'].value,
        'cabelo': form['cabelo'].value}

for field in ('nome', 'idade', 'tamanho', 'politica', 'comentario'):
    if not field in form:
        data[field] = '(unknown)'
    else:
        if not isinstance(form[field], list):
            data[field] = form[field].value
        else:
            values = [x.value for x in form[field]]
            data[field] = ' e '.join(values)

print(html % data)
