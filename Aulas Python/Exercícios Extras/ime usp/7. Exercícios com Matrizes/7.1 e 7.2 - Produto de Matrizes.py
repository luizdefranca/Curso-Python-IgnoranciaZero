def main ():
    m = int(input("Digite o número de linhas da matriz A: "))
    n = int(input("Digite o número de colunas da matriz A: "))
    A = forme_matriz(m,n)
    p = int(input("Digite o número de colunas da matriz B: "))
    B = forme_matriz(n,p)
    produto = []
    for i in range(m):
        linha = []
        for k in range(p):
            ele = 0
            for j in range(n):
                ele += A[i][j]*B[j][k]
            linha.append(ele)
        produto.append(linha)
    print(produto)

def forme_matriz(lin,col):
    matriz = []
    for i in range(lin):
        linha = []
        for j in range (col):
            ele = float(input("Digite o elemento a%d%d da matriz: "%(i+1,j+1)))
            linha.append(ele)
        matriz.append(linha)
    return matriz
main ()
