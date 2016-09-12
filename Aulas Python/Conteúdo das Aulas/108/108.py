"""
system = permite executar um comando
popen = permite inserir comandos mas direcionar sua saída
startfile = abre arquivo no programa default
"""
import os, sys

if 'win' in sys.platform:
    print("os.system('type arquivo.txt') = ",os.system('type arquivo.txt'))
else:
    print("os.system('cat arquivo.txt') = ",os.system('cat arquivo.txt'))

input()

print("os.system('dir %s'%os.getcwd()) = ",os.system('dir %s'%os.getcwd()))
input()

print("os.system('dir x') = ",os.system('dir x'))
input()

if 'win' in sys.platform:
    print("os.popen('type arquivo.txt') = ", os.popen('type arquivo.txt'))
else:
    print("os.popen('cat arquivo.txt') = ",os.popen('cat arquivo.txt'))
input()

if 'win' in sys.platform:
    print("os.popen('type arquivo.txt').read() = ",os.popen('type arquivo.txt').read())
else:
    print("os.popen('cat arquivo.txt').read() = ",os.popen('cat arquivo.txt').read())
input()

print("os.popen('dir %s'%os.getcwd()).readlines() = ",os.popen('dir %s'%os.getcwd()).readlines())
input()

print("os.popen('dir x').read() = ",os.popen('dir x').read())
input()

input('Startfile --> Só para windows')

if 'win' in sys.platform:
    os.startfile('ex' + os.sep + 'sons' + os.sep + 'som_test.wav')


