"""
Peça uma lista de números inteiros para o usuário
e imprima a lista sem repetições
"""

n = int(input("Digite o número de elementos da lista: "))

lista = []
aux = []

for i in range(n):
    elemento = int(input("Digite o elemento %i de %i: "%(i+1, n)))
    lista.append(elemento)
    aux.append(elemento)

print(lista)

for ele in aux:
    aparições = lista.count(ele)
    for i in range(aparições-1):
        lista.remove(ele)

print(lista)

