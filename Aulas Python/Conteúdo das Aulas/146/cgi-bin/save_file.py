#!/usr/bin/python
# coding: UTF-8

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

# Primeiro nós verificamos se um arquivo foi selecionado
if fileitem.filename:
   # Em seguida verificamos se o diretório de arquivos foi criado
   if not os.path.exists(os.path.join(os.getcwd(), 'tmp')):
      # Senão nós o criamos
      os.mkdir(os.path.join(os.getcwd(), 'tmp'))

   # Nós removemos do nome do arquivo o caminho no diretório do cliente
   fn = os.path.basename(fileitem.filename)

   # Em seguida nós escrevemos o arquivo no servidor
   open(os.path.join(os.getcwd(), 'tmp', fn), 'wb').write(fileitem.file.read())

   # Criamos a mensagem a ser disponibilizada
   mensagem = 'O arquivo "' + fn + '" foi enviado com sucesso!'
   
else:
   mensagem = 'Nenhum arquivo foi selecionado'
   
print("""\
Content-Type: text/html\n
<html>
<body>
   <p>%s</p>
</body>
</html>
""" % mensagem
)
