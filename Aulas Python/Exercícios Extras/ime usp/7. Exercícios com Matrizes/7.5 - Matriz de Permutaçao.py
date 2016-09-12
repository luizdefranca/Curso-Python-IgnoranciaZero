def main ():
    n = int(input("Digite o número de colunas da matriz A: "))
    A = forme_matriz(n,n)
    resp = True
    i = 0
    while resp and i < n:
        linha = []
        linha = A[i]
        cont_0 = cont_1 = 0
        for j in range(n):
            if linha[j] == 0:
                cont_0 += 1
            elif linha[j] == 1:
                cont_1 += 1
            else:
                resp = False
        if cont_0 != n - 1:
            resp = False
        i += 1
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
