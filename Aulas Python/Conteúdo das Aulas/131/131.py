import os

print("Queues")

input()

print("Queue significa 'fila' em inglês e")
print("consiste num módulo que organiza o acesso")
print("a um tipo de data qualquer")

input()

print("Queues em python são modeladas por")
print("um objeto que obdece a regra FIFO")
print("(first in first out) que indica que")
print("o primeiro objeto a entrar na fila")
print("será também o primeiro a sair da fila")

input()

print("Filas são semelhantes a listas")
print("no sentido de serem fontes de")
print("armazenamento de objetos, entretanto")
print("diferente de listas são automaticamente")
print("controladas por uma thread lock")

input()

print("Veja o exemplo a seguir")

input()

os.system("python3 fila.py")

input()

print("Note que nós usamos o módulo")
print("_thread ao invés do módulo threading")
print("isso ocorre porque por definição o programa")
print("não irá sair enquanto as threads estiverem")
print("sendo executadas, entretanto pelo _thread")
print("o programa fecha silenciosamente quando")
print("quando a thread principal fecha, mesmo que")
print("as outras threads ainda estejam rodando")
print("em seus loops infinitos")

input()

print("Alternativamente, poderiamos modelar")
print("isso usando o modulo threading ao especificar")
print("a sua flag daemon para verdadeiro, pois")
print("threads com daemon=False irão previnir o")
print("programa de ser fechado")

input()

print("Veja o exemplo a seguir")

input()

os.system("python3 fila_threading.py")

input()

