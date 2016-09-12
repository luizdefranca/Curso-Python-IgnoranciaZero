import sys
import http.client

# Número de linhas a serem mostradas
showlines = 50

# Primeiro nós obtemos o servidor e o arquivo
# que nós desejamos obter deste (o arquivo pode
# ser uma página da web)
try:
    servidor, arquivo = sys.argv[1:]
except:
    servidor, arquivo = 'google.com', '/index.html'

# Imprimimos o conteúdo a ser exibido
print(servidor, arquivo)

# Inicializamos a conexão com o servidor utilizando o
# objeto HTTPConnection
server = http.client.HTTPConnection(servidor)

# Nós mandamos para o servidor um comando para
# tentar obter o arquivo desejado.
server.putrequest('GET', arquivo)
server.putheader('Accept', 'text/html')
server.endheaders()

# Obtem resposta do servidor depois de inserir
# o requirimento para obter o arquivo. Aqui podem
# aparecer diversos tipos de erros, que você já
# conhece, por exemplo 404.
resposta = server.getresponse()

# Se o requerimento foi feito com sucesso nós obteremos
# o código 200
if resposta.status != 200:
    # Caso o requerimento não tenha sido feito com sucesso
    # nós imprimimos o erro obtido
    print('Error sending request', resposta.status, resposta.reason)
else:
    # Caso contrário, nós lemos o conteúdo do arquivo
    data = resposta.readlines()
    resposta.close()

    # Imprime as linhas obtidas do arquivo
    for linha in data[:showlines]:
        print(linha)
