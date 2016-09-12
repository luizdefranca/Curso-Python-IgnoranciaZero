from socket import *

def main():
    # Cria host e port number
    host = "localhost"
    port = 5000

    # O servidor será um par endereço e port
    server = (host, port)

    # Criamos o socket
    conexão = socket(AF_INET, SOCK_DGRAM)
    conexão.bind((host, port))

    # Vamos mandar menssagem enquanto a menssagem for diferente de sair (s)
    msg = input("-> ")
    while msg != 's':
        # Mandamos a menssagem através da conexão
        conexão.sendto(msg.encode(), server)

        # Recebemos uma respota do servidor
        data, endereço = conexão.recvfrom(1024)

        # Imprimimos a menssagem recebida
        print("Recebida ->", str(data))

        # Podemos mandar mais menssagens
        msg = input("-> ")

    # Fechamos a conexão
    conexão.close()

if __name__ == '__main__':
    main()
