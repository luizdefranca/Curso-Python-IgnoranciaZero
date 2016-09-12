"""
Escreva uma função que troca um elemento por outro numa matriz
"""
matriz = []
m = int(input("Digite o número de linhas da matriz: "))
n = int(input("Digite o número de colunas da matriz: "))

def constróiMatriz(m, n, matriz):
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            x = int(input("Digite o elemento %i%i da matriz: "%(i,j)))
            linha.append(x)

        matriz.append(linha)

def TrocaElemento(pos1, pos2, matriz):
    elemento1 = matriz[pos1//10 -1][pos1%10 -1]
    elemento2 = matriz[pos2//10 -1][pos2%10-1]
    matriz[pos1//10-1][pos1%10-1] = elemento2
    matriz[pos2//10-1][pos2%10-1] = elemento1

constróiMatriz(m, n, matriz)
print(matriz)
pos1 = int(input("Digite a posição do elemento 1: "))
pos2 = int(input("Digite a posição do elemento 2: "))
TrocaElemento(pos1, pos2, matriz)
print(matriz)
