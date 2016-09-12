import socket
import threading
import os

def RetemArquivo(nome, sock):
    """
    Função que devolve um determinado arquivo
    Recebe o nome do arquivo a ser devolvido
    e a conexão estabelecida sock
    """
    # Obtemos o nome do arquivo lendo os dados enviados
    # pelo socket
    nome_arquivo = sock.recv(1024)

    # Verificamos se o arquivo existe
    if os.path.isfile(nome_arquivo):
        # Se o arquivo existir mandamos uma resposta dizendo que
        # ele existe e o tamanho total do arquivo
        sock.send("EXISTE " + str(os.path.getsize(nome_arquivo)))

        # Em seguidas recebes mais dados do usuário dizendo
        # se o arquivo deve ser enviado ou não
        reposta_user = sock.recv(1024)

        # Se o arquivo deve ser enviado nós
        if reposta_user[:2] == 'OK':
            # Abrimos o arquivo no formato de bytes
            with open(nome_arquivo, 'rb') as arq:
                # Lemos os dados do arquivo para enviar
                bytes_a_enviar = arq.read(1024)

                # Enviamos através do socket
                sock.send(bytes_a_enviar)
 
                # Até que não haja mais bytes no arquivo
                while bytes_a_enviar != "":
                    bytes_a_enviar = f.read(1024)
                    sock.send(bytes_a_enviar)
    else:
        # Se ele não existe enviamos uma menssagem de erro
        sock.send("ERRO ")

    # Fechamos a conexão
    sock.close()

def main():
    # Host e port number do server
    host = '127.0.0.1'
    port = 5000

    # Abrimos um socket para o server
    s = socket.socket()
    s.bind((host,port))

    # Esperamos ouvir 5 conexões
    s.listen(5)

    # Informamos que o servidor foi iniciado
    print("Servidor Iniciado")
 
    # Bloco infinito do servidor
    while True:
        # Esperamos uma nova conexão
        c, endereço = s.accept()
        print "Cliente conectado ip:<" + str(endereço) + ">"

        # Iniciamos uma nova thread para se comunicar com o cliente
        t = threading.Thread(target=RetemArquivo, args=("RetemArquivo", c))
        t.start()
    
    # Fecha o servidor
    s.close()

if __name__ == '__main__':
    main()
