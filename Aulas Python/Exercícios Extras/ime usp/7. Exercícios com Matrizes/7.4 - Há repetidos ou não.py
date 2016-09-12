def main ():
    m = int(input("Digite o número de linhas da matriz A: "))
    n = int(input("Digite o número de colunas da matriz A: "))
    A = forme_matriz(m,n)
    resp = False
    i = 0
    while not resp and i < m:
        for j in range(m):
            for k in range(i,m):
                for l in range(n):
                    if A[i][j] == A[k][l] and k != i and l!=j:
                        resp = True
        i += 1
    print(resp)

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
