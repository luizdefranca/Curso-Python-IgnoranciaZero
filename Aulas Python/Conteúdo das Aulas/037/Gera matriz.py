"""
Escreva uma função que gera uma matriz 4x4 com os números de 0 a 15 sem
repetições
"""

import random
matriz = []
def geraMatriz(matriz):
    lista = list(range(16))
    for j in range(4):
        linha = []
        for i in range(4):
            x = random.choice(lista)
            linha.append(x)
            lista.remove(x)
        matriz.append(linha)

for i in range(3):
    matriz = []
    geraMatriz(matriz)
    print(matriz)
