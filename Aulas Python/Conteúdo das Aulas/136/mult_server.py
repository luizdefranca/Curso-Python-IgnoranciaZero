import time, _thread as thread

from socket import *

# Cria o nome do host
meuHost = ''

# Utiliza este número de porto
minhaPort = 50007

# Cria um objeto socket. As duas constantes referem-se a:
# Familia do endereço (padrão é socket.AF_INET)
# Se é stream (socket.SOCK_STREAM, o padrão) ou datagram (socket.SOCK_DGRAM)
# E o protocolo (padrão é 0)
# Da maneira como configuramos:
# AF_INIT == Protocolo de endereço de IP
# SOCK_STREAM == Protocolo de transferência TCP
# Combinação = Server TCP/IP
sockobj = socket(AF_INET, SOCK_STREAM)

# Vincula o servidor ao número de porto
sockobj.bind((meuHost, minhaPort))

# O socket começa a esperar por clientes limitando a 
# 5 conexões por vez
sockobj.listen(5)

def agora():
    # Devolve o tempo
    return time.ctime(time.time())

def lidaCliente(conexão):
    # Simula atividade no bloco
    time.sleep(5)
    
    while True:
        # Recebe data enviada pelo cliente
        data = conexão.recv(1024)
        
        # Se não receber nada paramos o loop
        if not data: break
        
        # Escreve a resposta
        resposta = 'Eco=>%s as %s' % (data, agora())

        # O servidor manda de volta uma resposta
        conexão.send(resposta.encode())
    
    # Fecha a conexão criada depois de responder o
    # cliente
    conexão.close()

def despacha():
    # Ouve processos até
    while True:
        # Aceita uma conexão quando encontrada e devolve a
        # um novo socket conexão e o endereço do cliente
        # conectado
        conexão, endereço = sockobj.accept()
        print('Server conectado por', endereço, end=' ')
        print('as', agora())

        # Inicia nova thread para lidar com o cliente
        thread.start_new_thread(lidaCliente, (conexão,))

despacha()
