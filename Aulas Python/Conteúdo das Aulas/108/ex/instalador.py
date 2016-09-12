import os, sys

p = os.path.abspath("aplicativo")

NOME = input('Seu nome: ')

NOME = os.path.join(os.getcwd(), 'Python-'+NOME)
os.rename(p, NOME)

if 'win' in sys.platform:
    d = os.path.join('c:', 'users', os.environ['USER'])
    os.system('copy %s %s'%(NOME, d))
    os.startfile('leiame.txt')

else:
    os.system('cp -r %s -t ~'%NOME)
    os.system('gedit leiame.txt')

os.rename(NOME, "aplicativo")
