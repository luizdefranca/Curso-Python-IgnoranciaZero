#!/usr/bin/python
import cgitb; cgitb.enable()
print('Content-type: text/html\n')

print(
    """<html>
	<head>
		<title>CGI 5 - Tabelas</title>
	</head>
	
	<body>
		<h1>Adicionando tabelas</h1>
		
		<hr>
			<p>Ola tabelas CGI!</p>
			
			<table border=1>"""
)

for i in range(5):
    print(4*'\t'+'<tr>')
    for j in range(4):
        print(5*'\t'+'<td>%d.%d</td>' % (i, j))
    print(4*'\t'+'<tr>')

print("""			</table>
		<hr>
	</body>
</html>
"""
)
