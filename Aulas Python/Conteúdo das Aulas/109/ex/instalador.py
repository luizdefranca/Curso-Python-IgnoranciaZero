"""
Argumentos específicados:
    -d diretorio = Escolhe diretório de destino
    -n nome = Escolhe renomeamento do arquivo
"""

argumentos = {}

def getArg(flag):
    """
    Devolve o argumento de uma dada flag
    """
    try:
        a = sys.argv[sys.argv.index(flag) + 1]
    except:
        return ""
    else:
        return a

import os, sys

p = os.path.abspath("aplicativo")

if '-d' in sys.argv:
    argumentos['d'] = getArg('-d')
    
if '-n' in sys.argv:
    argumentos['n'] =  getArg('-n')

if 'n' not in argumentos:
    argumentos['n'] = input('Seu nome: ')
    argumentos['n'] = os.path.join(os.getcwd(), 'Python-'+argumentos['n'])

if 'd' not in argumentos: 
    if 'win' in sys.platform:
        argumentos['d'] = os.path.join('c:', 'users', os.environ['USER'])
    else:
        argumentos['d'] = '~'

os.rename(p, argumentos['n'])

if 'win' in sys.platform:
    os.system('copy %s %s'%(argumentos['n'], argumentos['d']))
    os.startfile('leiame.txt')

else:
    os.system('cp -r %s -t %s'%(argumentos['n'], argumentos['d']))
    os.system('gedit leiame.txt')

os.rename(argumentos['n'], "aplicativo")
