def main ():
    n = int(input("Digite a ordem da matriz A: "))
    A = forme_matriz(n,n)
    print (A)
    magico = d_p = d_s = 0
    for i in range(n):
        magico += A[0][i]
    #linhas e colunas
    resp = True
    i = 0
    while resp and i < n:
        linha = coluna = 0
        for j in range(n):
            linha += A[i][j]
            coluna += A[j][i]
        if linha != magico or coluna != magico:
            resp = False
        i += 1
    #diagonal principal
    for i in range(n):
        d_p += A[i][i]
    #diagonal secundaria
    i, j = 0, 2
    while i< n and j > -1:
        d_s += A[i][j]
        i += 1
        j -=1
    if d_p != magico or d_s != magico:
        resp = False
    print (resp)
        
        
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
