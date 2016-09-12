def main ():
    m = int(input("Digite o número de linhas da matriz A: "))
    n = int(input("Digite o número de colunas da matriz A: "))
    A = forme_matriz(m,n)
    cont_l = cont_c = 0
    for i in range(m):
        cont_0l = cont_0c = 0
        for j in range(n):
            if A[i][j] == 0:
                cont_0l += 1
            if A[j][i] == 0:
                cont_0c += 1
        if cont_0l == m:
            cont_l +=1
        if cont_0c == n:
            cont_c += 1
    print("O numero de linhas nulas é %d e o numero de colunas nulas é %d"%(cont_l,cont_c))


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
