import nntplib

# Lista de headers que nós desejamos imprimir
showhdrs = ['From', 'Subject', 'Date', 'Newsgroups', 'Lines']

try:
    # Podemos obter as configurações do servidor passando-as
    # como parâmetros da linha de comando durante a execução
    # do programa
    import sys
    nome_servidor, nome_grupo, mostra_contador = sys.argv[1:]
    
except:
    # Caso o servidor não seja configurado a partir de argumentos
    # temos uma configuração padrão
    nome_servidor = 'news.gmane.org'
    nome_grupo = 'gmane.comp.python.committers'

# Realiza a conexão com o servidor
print('Conectando com', nome_servidor, 'para', nome_grupo)
conexão = nntplib.NNTP(nome_servidor)
(reply, conta, primeiro, último, nome) = conexão.group(nome_grupo)
print('%s possuí %s artigos: %s-%s' % (nome, conta, primeiro, último))

# Obtem todos os assuntos tratados no intervalo
# considerado (no nosso caso, todas as mensagens
# no repositório)
(reply, assuntos) = conexão.xhdr('subject', (str(primeiro) + '-' + str(último)))

# Obtem o corpo das mensagens
for (idnt, subj) in assuntos:
    # Imprimimos a identificação da postagem e o
    # assunto da postagem
    print('Artigo %s [%s]' % (idnt, subj))

    # Obtem o id da menssagem
    resp, number, id_mensagem = conexão.stat(idnt)

    # Imprimimos os conteúdos da mensagem
    if input('=> Deseja ler a mensagem?') in ['s', 'S']:
        resp, info = conexão.head(id_mensagem)
        for i in range(len(info.lines)):
            linha = info.lines[i].decode()
            for h in showhdrs:
                if h in linha:
                    print(linha)
                    break

        if input('=> Deseja mostrar o conteúdo?') in ['s', 'S']:
            resp, info = conexão.body(id_mensagem)
            print(80*'-')
            for i in range(len(info[2])):
                print(info[2][i].decode())
            print(80*'-')

    print()

print(conexão.quit())
