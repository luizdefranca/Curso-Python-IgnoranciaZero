"""
Servidor: Lida com múltiplos clientes em paralelo com select. Usa select
para manualmente lidar com um conjunto de sockets: Sockets principais que
aceitam novas conexões, e sockets de input conectadas para aceitar clientes.
"""

import time
from select import select
from socket import socket, AF_INET, SOCK_STREAM

def agora(): return time.ctime(time.time())

# Configurações do servidor
meuHost = ''
minhaPort = 50007

# Número de sockets usados
numPortSocks = 2

# Lista de sockets criados por função de cada socket
socks_principais, le_socks, escreve_socks = [], [], []

# Cria um socket para cada função
for i in range(numPortSocks):
    # Configura um socket TCP/IP
    portsock = socket(AF_INET, SOCK_STREAM)

    # Configura o socket
    portsock.bind((meuHost, minhaPort))
    portsock.listen(5)

    # O adiciona a lista de principais e leitoras
    socks_principais.append(portsock)
    le_socks.append(portsock)

    # Aumenta o valor da port para mudar o próximo socket
    minhaPort += 1

print('Loop de seleção de socket iniciado')

while True:
    # Vemos todos os sockets legiveis e escreviveis e os selecionamos
    legiveis, escreviveis, excessões = select(le_socks, escreve_socks, [])
    
    # Para cada socket legivel
    for sockobj in legiveis:
        # Se ele é um socket principal
        if sockobj in socks_principais:
            # Aceita o socket
            novo_sock, endereço = sockobj.accept()
            # Imprime as conexões
            print('Conecta:', endereço, id(novo_sock))
            # E o coloca no socket de leitura
            le_socks.append(novo_sock)
     
        else:
            # Lemos o que está no socket
            data = sockobj.recv(1024)

            # Imprime a menssagem recebida
            print('\tRecebeu', data, 'em', id(sockobj))
            
            # Se não recebermos nada
            if not data:
                # Fechamos o socket
                sockobj.close()
                # E o removemos do socket de leitura
                le_socks.remove(sockobj)
            # Caso contrário
            else:
                # Preparamos uma resposta a ser enviada
                resposta = 'Eco=>%s as %s' % (data, agora())
                sockobj.send(resposta.encode())
