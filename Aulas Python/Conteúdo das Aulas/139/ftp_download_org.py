"""
Este arquivo organiza as funcionalidades para
baixar arquivos numa única função
"""

from ftplib import FTP
from os.path import exists

def getfile(file, site, dir, user=(), *, verbose=True, refetch=False):
    """
    Obtem um arquivo de um determinado site no diretório
    selecionado
    ;paramn file: str nome do arquivo a ser baixado
    ;paramn site: str domínio do servidor
    ;paramn user: tuple contendo o usuário e senha, se estiver
                  vazia o login é feito no modo anonimo
    ;paramn verbose: bool indicando se devem ser impressas mensagens
                     indicando as operações realizadas
    ;paramn refetch: bool indicando se caso o arquivo exista se ele
                     deve ser baixado novamente
    """

    # Primeiro verificamos se o arquivo existe, se for o caso
    # e nós não estivermos no modo refetch devemos sair da função
    if exists(file) and not refetch:
        if verbose: print(file, 'já foi baixada')
        return
    else:
        if verbose: print('Downloading', file)
    
    # Abre o arquivo local
    local = open(file, 'wb')
    
    # Encapsulamos as operações de download num bloco de try
    # uma vez que é necessário lidar com possíveis erros de
    # conexão
    try:
        # Cria a conexão com servidor 
        remote = FTP(site)
        # Realiza o login
        remote.login(*user)
        # Muda diretório
        remote.cwd(dir)
        # Baixa o arquivo no modo binário
        remote.retrbinary('RETR ' + file, local.write, 1024)
        # Fecha a conexão
        remote.quit()
    finally:
        # Fecha o arquivo local
        local.close()

        if verbose: print('Download Concluído.')
