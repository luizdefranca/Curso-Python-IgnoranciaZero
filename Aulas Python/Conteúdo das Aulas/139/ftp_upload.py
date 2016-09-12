import ftplib

def manda_arquivo(arq, site, dir, usuario=(), *, verbose=True):
    """
    Salva um arquivo utilizando o ftp para um site
    ou diretório por meio anônimo ou como um usuário
    autenticado.
    """
    # Verbose indica se devemos mostrar menssagens indicando
    # o progresso do aplicatiovo
    if verbose: print('Enviando', arq)
    
    # Abre o arquivo a ser enviado
    local = open(arq, 'rb')

    # Abre uma nova conexão ftp
    remote = ftplib.FTP(site)

    # Faz login no servidor
    remote.login(*usuario)

    # Muda para o diretório a ser feito o upload
    remote.cwd(dir)

    # Começa a fazer upload do arquivo
    remote.storbinary('STOR ' + arq, local, 1024)

    # Fecha conexão
    remote.quit()
    local.close()
    
    # Indica que o envio terminou
    if verbose: print('Envio terminado.')

if __name__ == '__main__':
    # Domínio que devemos acessar
    site = 'ftp.rmi.net'

    # Diretório do upload
    dir = '.'

    # Pedimos para o usuário o nome do arquivo
    arq = input("Nome do arquivo? ")

    # Pedimos para o usuário a senha
    import getpass
    senha = getpass.getpass(site + ' Senha?')

    # Enviamos o arquivo
    manda_arquivo(arq, site, dir, user=('lutz', senha))
