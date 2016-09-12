"""
Argumentos específicados:
    -d diretorio = Escolhe diretório de destino
    -n nome = Escolhe renomeamento do arquivo
"""

import os, sys, argparse

#Cria a parte de controle de argumentos
parser = argparse.ArgumentParser(description="Instalador do aplicativo desenvolvido em aula")
parser.add_argument("-d", "--directory", help="Diretório de instalação", action="store")
parser.add_argument("-n", "--name", help="Nome do aplicativo", action="store")
args = parser.parse_args()


#Lida com os argumentos para nome
if args.name == None:
    nome = 'Python-iz'
else:
    nome = args.name

#Lida com os argumentos para diretório
if args.directory == None: 
    if 'win' in sys.platform:
        d = os.path.join('c:', 'users', os.environ['USER'])
    else:
        d = os.path.join("/home", os.environ["USER"])
else:
    d = args.directory

#Copia a pasta para o caminho específicado
if 'win' in sys.platform:
    os.system('copy %s %s'%(nome, d))
    os.startfile('leiame.txt')
else:
    os.system('cp -r %s -t %s'%("aplicativo", d))
    os.system('gedit leiame.txt')

#Muda o diretório para pasta de instalação
os.chdir(d)

#Renomeia a pasta para o nome específicado
os.rename("aplicativo", nome)
