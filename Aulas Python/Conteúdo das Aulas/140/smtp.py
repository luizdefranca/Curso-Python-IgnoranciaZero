import smtplib
import sys
import email.utils
import mailconfig
import getpass

# Configura o servidor SMTP
mailserver = mailconfig.servidor_smtp
mailport = mailconfig.port_smtp
mailuser = mailconfig.usuário_smtp

# Obtem a senha para o servidor smtp
mailpasswd = getpass.getpass('Senha para %s?' % mailserver)

# Pede pela as opções de destinatário e remetente
# que também poderiam ser obtidas a partir do arquivo
# mailconfig. Note que podemos ter vários destinatários
# basta separa-los por ;
De = input('De? ').strip()
Para = input('Para? ').strip()
Paras = Para.split(';')

# Configuramos o assunto da mensagem que informamos a data
# em formato de rfc2822
Assunto = input('Assunto? ').strip()
Data = email.utils.formatdate()

# Criamos os headers de emails padrão
texto = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' % (De, Para, Data, Assunto))

# Começamos a escrever o conteúdo da mensagem
print('Escreva a mensagem, fim de linha dado por=[Ctrl+d (Unix), Ctrl+d (Windows)]')
while True:
    # Recebemos uma linha digitada pelo usuário
    linha = sys.stdin.readline()

    # Se o usuário terminar de preencher o texto e fornecer uma linha vazia
    # obtivemos podemos encerrar a mensagem
    if not linha: break

    # Adicionamos ao texto a linha escrita
    texto += linha

# Iniciamos a conexão com o servidor SMTP
print('Conectando...')
server = smtplib.SMTP(mailserver, mailport)

# Novamente, para efeitos didáticos estaremos conectando
# com o gmail. O servidor SMTP do gmail pode ter a configuração
# de um protocolo de criptografia por cima do tipo TLS ou SSL.
# no caso utilizamos a port 587, que configura um servidor
# TLS (poderíamos usar a port 465 para SSL), e, para servidores
# deste tipo, é preciso chamar o método "starttls" antes de começar
# as operações.
server.starttls()

# Além disso como se trata do servidor do google, é preciso
# logar no mesmo
server.login(mailuser, mailpasswd)

# Tentamos mandar o email conforme as configurações fornecidas pelo
# usuário
falhou = server.sendmail(De, Paras, texto)

# Encerramos a conexão com o servidor smtp
server.quit()

# Se o envio do email tiver falhado nós imprimimos uma mensagem
# informando os problemas encontrados
if falhou:
    print('Envio Falhou:', falhou)
else:
    print('Enviado com Sucesso.')
