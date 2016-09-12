"""
getpid = ID do processo que está executando
getcwd = recebe o diretório de trabalho atual
remove = remove um arquivo
rename = renomeia um arquivo
urandom(n) = retorna n bytes de cryptografada fortemente uma data aleatória

CONSTANTES
    pathsep = separador de caminhos
    sep = separador de diretórios
    pardir = caminho de volta para diretório
    curdir = código para obter diretório atual
    linesep = separador de linhas
    environ = dicionário com caminhos e configurações específicas do sistema

tkinter.PhotoImage(file = 'Imagens'+ os.sep + 'foto.pgm')
"""

import os, sys

input('ID do programa e o diretório de trabalho')
print(os.getpid(), os.getcwd())
input()
"""
input('Vá na pasta e veja que o arquivo vai ser renomeado')
os.rename('arquivo', 'renomeado')
input()

input('Vamos remover também o arquivo')
os.remove('renomeado')
input()
"""
input('Gera uma string aleatória e criptografada')
print(os.urandom(5))
input()

input('Constantes especiais para diretórios')
x = os.pathsep, os.sep, os.pardir, os.curdir, os.linesep
print(x)
input()

input('Dicionário com as configurações do sistema')
print(list(os.environ.keys()))
input()

input('Valor de uma das chaves do dicionário')
if 'win' in sys.platform:
    print(os.environ['PYTHONPATH'])
    print(os.environ['TEMP'])
else:
    print(os.environ['LANGUAGE'])

print(os.environ['USER'])
input()

input('Modificação dos valores da chave')
os.environ['USER'] = 'João'
print(os.environ['USER'])
input()

