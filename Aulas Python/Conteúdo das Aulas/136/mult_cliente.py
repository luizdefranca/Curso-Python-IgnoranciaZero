from socket import *
import threading

class Cliente(threading.Thread):
    """
    Classe que gera os clientes
    """
    def __init__(self, c, server, port, *menssagem):
        # Número de identificação do cliente
        self.c = c

        # Servidor a ser conectado
        self.server = server

        # Port para ser usada
        self.port = port

        # Menssagens a serem colocadas
        self.msgs = menssagem

        threading.Thread.__init__(self)

    def run(self):
        # Criamos o socket e o conectamos ao servidor
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.connect((self.server, self.port))

        # Mandamos a menssagem linha por linha
        for linha in self.msgs:
            sockobj.send(linha)

            # Depois de mandar uma linha esperamos uma resposta
            # do servidor
            data = sockobj.recv(1024)
            print('Cliente', self.c, 'recebeu:', data)

        # Fechamos a conexão
        sockobj.close()


# Configurações de conexão do servidor
# O nome do servidor pode ser o endereço de
# IP ou o domínio (ola.python.net)
serverHost = 'localhost'
serverPort = 50007

# Menssagem a ser mandada condificada em bytes
menssagem = [b'Ola mundo da internet!']

# Nós spawnamos os clientes
for c in range(20):
    Cliente(c, serverHost, serverPort, *menssagem).start()

print("Geramos todos os clientes")
