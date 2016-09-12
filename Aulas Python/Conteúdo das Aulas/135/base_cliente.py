"""
Lado do cliente: Usa sockets para mandar data para o servidor, e imprime
a resposta do servidor para cada linha na mensagem. Podemos colocar o 
host como sendo localhost para indicar que o servidor está na mesma máquina.
Para rodar através da internet é preciso colocar o servidor em outra
máquina e passar para o nome do host o endereço de IP ou o nome do
domínio.
"""

from socket import *

# Configurações de conexão do servidor
# O nome do servidor pode ser o endereço de
# IP ou o domínio (ola.python.net)
serverHost = 'localhost'
serverPort = 50007

# Menssagem a ser mandada condificada em bytes
menssagem = [b'Ola mundo da internet!']

# Criamos o socket e o conectamos ao servidor
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

# Mandamos a menssagem linha por linha
for linha in menssagem:
    sockobj.send(linha)

    # Depois de mandar uma linha esperamos uma resposta
    # do servidor
    data = sockobj.recv(1024)
    print('Cliente recebeu:', data)

# Fechamos a conexão
sockobj.close()
