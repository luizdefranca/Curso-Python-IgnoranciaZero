def main ():
    m = int(input("Digite o número de linhas da matriz A: "))
    n = int(input("Digite o número de colunas da matriz A: "))
    A = forme_matriz(m,n)
    X = forme_matriz(n,1)
    produto = produto(A,X)
    print("Digite a matriz resultado: ")
    B = forme_matriz(m,1)
    resp = True
    for i in range (m):
        if produto[i][0] != B[i][0]:
            resp = False
    if resp:
        print("X é solução do sistema.")
    else:
        print("X não é solução do sistema")
    

def produto(A,B):
    produto = []
    for i in range(len(A)):
        linha = []
        for k in range(len(B[0]):
            ele = 0
            for j in range(len(A[0]):
                ele += A[i][j]*B[j][k]
            linha.append(ele)
        produto.append(linha)
    return produto
    

def forme_matriz(lin,col):
    matriz = []
    for i in range(lin):
        linha = []
        for j in range (col):
            ele = float(input("Digite o elemento a%d%d da matriz: "%(i+1,j+1)))
            linha.append(ele)
        matriz.append(linha)
    return matriz
