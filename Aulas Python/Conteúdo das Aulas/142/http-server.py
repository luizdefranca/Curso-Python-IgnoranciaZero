"""
Implementa um server HTTP em Python que sabe como utilizar paginas
HTML e rodar scripts CGI escritos em Python; Esse script foi escrito
com propósitos de teste em um ambiente local; Os scripts CGI devem
ser colocados no diretório webdir\cgi-bin ou webdir\htbin; Mais de 
um servidor pode ser executado para utilizar diferentes diretórios
e ports
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

# Diretório utilizado para manter arquivos HTML e scripts
# CGI
webdir = '.'

# Número de port, http://servername/ se 80, 
# senão use http://servername:xxxx/
port = 8080

# Adiciona o diretório de trabalho e a port se esses parâmetros
# forem fornecidos na linha de comando
if len(sys.argv) > 1: webdir = sys.argv[1]
if len(sys.argv) > 2: port = int(sys.argv[2])

# Imprime as configurações utilizadas
print('webdir "%s", port %s' % (webdir, port))

# Muda para o diretório de trabalho
os.chdir(webdir)

# Configura o endereço do servidor
srvraddr = ('', port)

# Cria o servidor HTTP com o Handler de HTTP
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)

# Espera receber algum comando a ser executado
srvrobj.serve_forever()
