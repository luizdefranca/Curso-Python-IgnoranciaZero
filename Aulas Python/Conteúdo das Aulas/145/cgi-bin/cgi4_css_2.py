#!/usr/bin/env python
import cgitb; cgitb.enable()
print('Content-type: text/html\n')
print(
    """<html>
	<head>
		<title>CGI 4 - CSS</title>
	
		<link rel="stylesheet" type="text/css" href="../css/estilo1.css">
	</head>


	<body>
		<h1>Colocando CSS em um script a parte</h1>
		<hr>
			<p>Ola imagens CGI!</p>

			<div class="wraptocenter">
	  			<img id="imagem" src="../imagens/evil.jpg" border=1 alt="Piadinha idiota" width=350 height=500>
			</div>
		<hr>
	</body>
</html>
    """
)
