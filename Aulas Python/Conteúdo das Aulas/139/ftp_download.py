"""
Um script para baixar e rodar um arquivo pelo FTP. Usa o ftplib, o objeto FTP
que utiliza sockets. FTP se basea em dois sockets (um para data, e outro para
controle-- nas ports 20 e 21) e impõe messagens com formatos específico, mas
o modulo ftplib esconde a maior parte dos detalhes desse protocolo. Mude o
endereço usado para o seu site/arquivo
"""

import os
from getpass import getpass
from ftplib import FTP

# Variavél que determina se devemos usar o modo ativo
# para FTP
nonpassive = False

# Nome do arquivo a ser baixado
nome_arquivo = 'README'

# Nome do diretório a ser acessado
dir_nome = 'debian'

# Nome do site a ser acessado, pode ser um domínio ou
# endereço de IP
site_nome = 'ftp.debian.org'

# Poderíamos pegar um usuário e senha para conectar
# no servidor
# usuario_info = ('lutz', getpass('Senha?'))
usuario_info = []
    
# Iniciamos a conexão
print('Conectando...')

# Criamos a conexão com o servidor do tipo FTP
# através do objeto FTP que recebe o endereço do
# servidor como argumento
conexão = FTP(site_nome)

# Fazemos o login com as informações do usuário
# Poderíamos utilizar o login sem nenhum argumento
# e desta forma estaríamos entrando no servidor
# anonimamente
conexão.login(*usuario_info)

# Acessamos um determinado diretório
conexão.cwd(dir_nome)

# Podemos listar os conteúdos do diretório corrente
# utilizando o método retrlines e passando para ele
# o comando LIST
print(conexão.retrlines('LIST'))

# Se devemos acessar os arquivos no modo passivo
# ou no modo ativo
if nonpassive:
    conexão.set_pasv(False)

# Iniciamos o download do arquivo
print('Baixando...')

# Abrimos um novo arquivo para armazenar as informações dos
# arquivos que estamos baixando
with open(nome_arquivo, 'wb') as arquivo_local:
    # Armazena informações do arquivo original no arquivo local
    
    # Colocamos a string 'RETR ' que indica o comando de download
    # para o FTP
    
    # retrbinary indica que estamos baixando o arquivo no modo
    # binário, poderíamos baixar o arquivo usando retrlines que baixa
    # o arquivo em ASCII
    conexão.retrbinary('RETR ' + nome_arquivo, arquivo_local.write, 1024)

    # Fechamos a conexão
    conexão.quit()

# Perguntamos se o usuário deseja abrir o arquivo, e se
# a reposta for sim nós o abrimos
if input('Abre Arquivo?').lower().startswith('s'):
    from PP4E.System.Media.playfile import playfile
    playfile(nome_arquivo)
