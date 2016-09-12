import os

for (nome, subs, arqs) in os.walk('.'):
    for fnome in arqs:
        if '~' in fnome:
            print('Diretório: [' + nome + ']')
            os.system("rm " + os.path.join(nome, fnome))
