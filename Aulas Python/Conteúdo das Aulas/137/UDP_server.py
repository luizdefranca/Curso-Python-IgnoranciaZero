from socket import *

def main():
    # Cria host e port number
    host = ""
    port = 5000

    # Cria socket
    server = socket(AF_INET, SOCK_DGRAM)

    # Indica que o servidor foi iniciado
    print("Servidor iniciado")

    # Bloco infinito do servidor
    while True:
        # Recebe a data e o endereço da conexão
        data, endereço = server.recvfrom(1024)
   
        # Imprime as informações da conexão
        print("Menssagem recebida de", str(endereço))
        print("Recebemos do cliente:", str(data))

        # Vamos mandar de volta a menssagem em eco
        resposta = "Eco=>" + str(data)
        server.sendto(data, endereço)
    
    # Fechamos o servidor
    server.close()

if __name__ == '__main__':
    main()
        
