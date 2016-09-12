#!/usr/bin/python

print('Content-type: text/html\n')
print("""
<html><title>Minha Pagina</title>
<body>
<form method=get action="download_fisico.py">
<h1>Escreva o nome do arquivo a ser visto</h1>
<p><input type=text size=50 name=filename>
<p><input type=submit value=Download>
</form>
<hr><a href="cgi-bin/download.py?filename=cgi-bin/download.py">Veja o codigo do Script</a>
</body></html>
"""
)
