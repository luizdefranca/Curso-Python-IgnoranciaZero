"""
chdir = muda o diretório de trabalho
mkdir = cria diretório
rmdir = remove um diretório vazio
listdir = lista todos os diretórios no diretório atual
walk = caminha por uma árvore de diretórios --> gerador
"""
import os

print("Antes de mais nada vejamos o diretório em que estamos")
print(os.getcwd())
input()

print("Agora que sabemos onde estamos podemos mudar de diretório")
print("Podemos fazer isso usando caminho relativo, por exemplo")
print("os.chdir('..')")
print(os.chdir('..'))
input()

print("Nosso diretório passa a ser")
print(os.getcwd())
input()

print("Vamos adiantar a próxima aula e criemos um novo diretório")
print("Diretório 114")
print(os.mkdir("114"))
input()

print("Bom vamos verificar se o diretório foi criado")
print(os.path.exists("114"))
input()

print("Agora vamos remover esse diretório")
print(os.rmdir("114"))
input()

print("Bom vamos verificar se o diretório foi removido")
print(os.path.exists("114"))
input()

print("Já fizemos muitas aulas até hoje, vejamos todas elas")
print(os.listdir())
input()

print("Legal né? Vamos olhar agora todo o conteúdo de nossas aulas")
print("Para isso temos que usar a função os.walk")
input("Aperte enter para ver a saída ")

for (nome, subs, arqs) in os.walk('.'):
    print()
    print('Diretório: [' + nome + ']')
    try:
        input("Aperte enter para ver os conteúdos do diretório: ")
    except EOFError:
        break
    for fnome in arqs:
        print("-->", os.path.join(nome, fnome))
