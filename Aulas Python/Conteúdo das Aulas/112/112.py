import sys
from io import StringIO
from io import BytesIO

print("Cria um buffer de strings")
buff = StringIO()
input()

print("Escreve 'spam\\n' no buffer ")
buff.write('spam\n')
input()

print("Escreve 'ovos\\n' no buffer ")
buff.write('ovos\n')
input()

print("Pega o valor contido no buffer")
print(buff.getvalue())
input()
#'spam\novos\n'

print("Cria o buffer já com um valor contido dentro dele")
buff = StringIO('presunto\nspam\n')
input()

print("Le uma linha do buffer")
print(buff.readline())
input()

print("Le outra linha do buffer")
print(buff.readline())
input()

print("Lemos todas as linhas do buffer, se tentarmos ler novamente veremos")
print("'" + buff.readline() + "'")
input()

print("Recriamos o buffer vazio")
buff = StringIO()
input()

print("Armazenamos o stdout numa variável temporária")
temp = sys.stdout
input()

print("Mandamos o sys.stdout = buff")
sys.stdout = buff
input()

print("Agora toda saida do print irá para o buff", file = temp)
print(42, 'spam', 3.141)
input()

print("Retormos o sys.stdout ao padrão", file = temp)
sys.stdout = temp
input()

print("Pegamos o valor no buffer")
print(buff.getvalue())
input()

print("Podemos usar o BytesIO de forma semelhante só que guardamos bytes ao invés de objetos strings")
input()

print("Criamos o stream")
stream = BytesIO()
input()

print("Escrevemos 'spam' dentro dele")
stream.write(b'spam')
input()

print("Imprimimos o valor")
print(stream.getvalue())
input()

print("Criamos um stream já com bytes de entrada")
stream = BytesIO(b'spam')
input()

print("Imprimimos novamente o stream")
print(stream.read())
input()

