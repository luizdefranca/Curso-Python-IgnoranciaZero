import socket

def main():
    # Cria o host e port number
    host = '127.0.0.1'
    port = 5000

    # Inicia a conexão com o servidor
    s = socket.socket()
    s.connect((host, port))

    # Espera o usuário digitar o nome do arquivo
    nome_arquivo = input("Nome do arquivo? -> ")

    # Se o usuário não digitou para fechar o programa
    if nome_arquivo != 'q':
        # Nós enviamos um requisito para o servidor
        s.send(nome_arquivo)

        # Recebemos uma resposta dele
        data = s.recv(1024)

        # Se a resposta for que o arquivo existe
        if data[:6] == 'EXISTE':
            # Armazenamos o tamanho do arquivo
            tamanho_arquivo = long(data[6:])

            # Perguntamos ao usuário se ele deseja baixar o arquivo
            msg = input("Arquivo existe, " + str(tamanho_arquivo) +"Bytes, baixar? (S/N)? -> ")
 
            # Se sim
            if msg == 'S':
                # Enviamos ao servidor que nós desejamos baixar o arquivo
                s.send("OK")

                # Criamos um novo arquivo no HD para baixa-lo
                arq = open('novo_'+nome_arquivo, 'wb')

                # Recebemos dados do arquivo pelo servidor
                data = s.recv(1024)

                # Vemos o tanto de informação que recebemos
                totalRecb = len(data)

                # Escrevemos no arquivo tudo o que escrevemos
                arq.write(data)

                # Enquanto não recebemos o equivalente ao tamanho do arquivo
                # em bytes
                while totalRecv < tamanho_arquivo:
                    # Continuamos a receber dados e escrever na cópia
                    data = s.recv(1024)
                    totalRecb += len(data)
                    arq.write(data)

                    # E imprimimos o status do download
                    print("{0:.2f}".format((totalRecb/float(tamanho_arquivo))*100)+ "% Terminado")

                # Avisamos quando o download terminou
                print("Download Terminado!")

                # E fechamos o arquivo
                arq.close()
        else:
            # Caso contrário avisamos que o arquivo em questão não existe
            print("Arquivo não Existe!")

    # Fechamos a conexão
    s.close()
    

if __name__ == '__main__':
    main()
