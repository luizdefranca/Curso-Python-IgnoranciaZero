import os

print("Forking é uma ferramenta exclusiva de sistemas")
print("de bases unix (linux, mac)")

input()

print("Forking consiste em criar uma cópia do programa")
print("e executar essa cópia em paralelo com a original")
print("por exemplo")

os.system("gedit teste.py")
os.system("python3 teste.py")

input()

os.system("gedit teste2.py")
os.system("python3 teste2.py")

input()

print("Note que dessa vez não travamos a execução do nosso")
print("programa, e temos programas executando em paralelo")

input()

print("Note que nos exemplos anteriores os novos programas")
print("simplesmente chamam uma função do programa original")
print("podemos também montar programas que são completamente")
print("independentes, ao utilizar a chamado da função os.exec__")

input()

os.system("gedit indp.py")
os.system("python3 indp.py")

input()

print("""
os.execv(programa, sequencialinhadecomando)
    O programa cujo nome é passado é executado com os argumentos passados, que pode ser uma lista ou tupla.

os.execl(programa, cmdarg1, cmdarg2,... cmdargN)
    É passado o nome do programa a ser executado com cada um dos argumentos da linha de comando passados como argumentos independentes da função

os.execlp
os.execvp
    Python irá localizar o diretório do executável usando o sistema de procura de caminhos.

os.execle
os.execve
    Permite um último argumento que consiste de variáveis de sistema a serem mandadas para o programa

os.execvpe
os.execlpe
    Combina as funcionalidades dos dois últimos
""")
