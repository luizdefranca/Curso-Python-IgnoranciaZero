import poplib
import getpass
import sys
import mailconfig

# Configuramos o servidor
mailserver = mailconfig.servidor_pop

# O nome do usuário
mailuser = mailconfig.usuário_pop

# Pedimos por uma senha
mailpasswd = getpass.getpass('Senha para %s?' % mailserver)

# Iniciamos o processo de conexão com o servidor
print('Conectando...')

# Por falta de exemplos práticos estaremos conectando no servidor
# do gmail. Para tanto utilizaremos um objeto especial o POP3_SSL
# ao invés do objeto clássico POP3. Esta diferença ocorre porque
# o servidor do google é implementado por cima de um socket
# criptografado com SSL. É preciso notar que o port para servidores
# desse tipo é, por default, 995, ao invés de 110 do POP3. O port
# pode ser configurado especialmente para cada servidor passando
# o parâmetro como uma string para a construção do objeto
server = poplib.POP3_SSL(mailserver)
server.user(mailuser)
server.pass_(mailpasswd)

# Uma vez conectado iniciamos o processo de recebimento de dados
try:
    # Se o servidor tiver alguma mensagem de boas vindas nós o
    # recebemos a partir do método "getwelcome"
    print(server.getwelcome())

    # Podemos obter dados do servidor utilizando o método stat
    msgCount, msgBytes = server.stat()

    # Imprimimos as informações recebidas
    print('Existem ', msgCount, 'mensagens de email em', msgBytes, 'bytes')

    # Aqui imprimimos as listas de mensagens com os bytes correspondentes
    # a cada uma delas
    print(server.list())

    # Esperamos o usuário querer prosseguir para ler o conteúdo das mensagens
    print('-' * 80)
    input('[Pressione Enter para Prosseguir]')

    # Iremos percorrer cada uma das mensagens contidas na caixa de email
    for i in range(msgCount):
        # Podemos ler o conteúdo das mensagens utilizando o método
        # retr e passando o número da mensagem que nós desejamos
        # obter
        hdr, mensagem, octets = server.retr(i+1)

        # Imprimimos todo o conteúdo da mensagem que acabamos de ler
        # só que temos que decodifica-la, uma vez que todo o texto de
        # email está em Bytes para o python 3.x
        for linha in mensagem: print(linha.decode())

        # Imprimimos um separador de conteúdo
        print('-' * 80)

        # Se nós não tivermos lido todas as mensagens ainda podemos
        if i < msgCount - 1:
            # Esperar o usuário pressionar enter para prosseguir com a
            # leitura de mensagens
            input('[Pressione Enter para Prosseguir]')
            
finally:
    # Nós fechamos a conexão com o email a partir
    # do método quit
    server.quit()
