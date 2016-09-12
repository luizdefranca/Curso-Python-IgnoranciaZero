#!/usr/bin/env python
import cgitb; cgitb.enable()
print('Content-type: text/html\n')
print(
    """<html>
	<head>
		<title>CGI 2 - Imagens</title>
	</head>


	<body>
		<h1>Colocando imagens por meio de CGI</h1>
		<hr>
			<p>Ola imagens CGI!</p>

	  		<img id="imagem" src="../imagens/evil.jpg" border=1 alt="Piadinha idiota" width=350 height=500>
		<hr>
	</body>
</html>
    """
)

'''
print("<title>CGI 2 - Imagens</title>")
print("<h1>Colocando imagens por meio de CGI</h1>")
print("<hr>")
print("<p>Ola imagens CGI!</p>")
print('<img id="imagem" src="../imagens/evil.jpg" border=1 alt="Piadinha idiota" width=350 height=500>')
print("<hr>")
'''
