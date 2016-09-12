#!/usr/bin/env python
import cgitb; cgitb.enable()
print('Content-type: text/html\n')
print(
    """<html>
	<head>
		<title>CGI 3 - CSS</title>
	
		<style>
			h1 {
			  color:red;
			}
			
			p {
                          color:blue;
			}
			
			.wraptocenter {
			  display: table-cell;
			  text-align: center;
			  vertical-align: middle;
			  width: 4000px;
			  height: 600px;
			  background-color: #fff;
			}
			.wraptocenter * {
			  vertical-align: middle;
			}
		</style>
	</head>


	<body>
		<h1>Colocando CSS na tag Style</h1>
		<hr>
			<p>Ola CSS CGI!</p>

			<div class="wraptocenter">
	  			<img id="imagem" src="../imagens/evil.jpg" border=1 alt="Piadinha idiota" width=350 height=500>
			</div>
		<hr>
	</body>
</html>
    """
)
