print("##### OrderedDict #####")

print("""
Na maioria das vezes, o que você está procurando realmente
em um dicionário é uma forma de mapear chaves específicas para
valores associados, de modo que a ordenação das chaves é irrelevante.
Às vezes, porém, também é útil ser capaz de iterar sobre essas
chaves de uma maneira confiável. Para oferecer o melhor dos dois mundos,
Python oferece a Classe OrderedDict por meio de seu módulo de collections.
Isso fornece todas as características de um dicionário, mas
com ordenação confiável das chaves.
""")
input()

print("Primeiro importamos")
from collections import OrderedDict
input()

print("Podemos criar um OrderedDict a partir da seguinte sintaxe:")
print("1 - Comprehension")
print("d = OrderedDict((value, str(value)) for value in range(10) if value > 5)")
d = OrderedDict((value, str(value)) for value in range(10) if value > 5)
print(d)
input()

print("2 - A partir de um objeto interável")
print("d = OrderedDict.fromkeys('abcde')")
d = OrderedDict.fromkeys('abcde')
print(d)
input()

print("Podemos modificar o valor das chaves:")
print("d['a'] = 5")
d['a'] = 5
print(d)
input()

print("Podemos obter todas as chaves")
print("d.keys()")
print(d.keys())
print("for k in d.keys(): print(k)")
for k in d.keys(): print(k)
input()

print("Podemos criar novas chaves:")
print("d['1'] = 18")
d['1'] = 18
print(d)
input()

print("Podemos mover a chave de posição")
print("d.move_to_end('b')")
d.move_to_end('b')
print(d)
print("d.move_to_end('b', last = False)")
d.move_to_end('b', last = False)
print(d)
input()

print("##### Heaps #####")

print("""
    Outra estrutura de dados conhecida é a heap, uma espécie de fila de prioridade. A fila de prioridade permite
você adicionar objetos em uma ordem arbitrária e em qualquer momento (possivelmente no meio da adição) encontrar
(e, possivelmente, remover) o menor elemento de maneira eficiente.

    Na verdade, não há nenhum built-in heap separado em Python - somente um módulo com algumas manipulações de heap.
O módulo é chamado heapq (com q significando queue = fila), que contém seis funções.
    """)

input()

from heapq import *
from random import shuffle

print("1 - heappush")
data = list(range(10))
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)
print(data, heap)
print("Lógica: Elemento na posiçãio i é menor que os na posição 2*i e 2*i + 1")
input()

for i in range(len(heap)):
    print("i:        ", i, "-->", heap[i])
    try:
        print("2i:       ", 2*i, "-->", heap[2*i])
        print("2i + 1:   ", 2*i + 1, "-->", heap[2*i + 1])
    except:
        break
    else:
        print()
input()

heappush(heap, 0.5)
print(heap)
input()

print("2 - heappop")
print("Remove o menor elemento")
print(heappop(heap))
print(heap)
print(heappop(heap))
print(heap)
print(heappop(heap))
print(heap)
input()

print("3 - heapify")
print("Tranforma uma lista abritária em algo adequado para uma heap")
heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
print(heap)
heapify(heap)
print(heap)
input()

print("4 - heapreplace")
print("Remove o menor elemento e adiciona um novo elemento ao heap")
heapreplace(heap, 0.5)
print(heap)
heapreplace(heap, 10)
print(heap)
input()

print("5 - nlargest e nsmallest")
print("""
nlargest(n, iter)
nsmallest(n, iter)
""")
print("Acham os n maior/menor elementos de um iterável qualquer")
input()

