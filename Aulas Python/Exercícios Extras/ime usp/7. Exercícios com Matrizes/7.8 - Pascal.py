def main ():
    n = int(input("Digite o número de linhas a ser impressa: "))
    pascal = []
    for j in range (n):
        linha = []
        for k in range (j+1):
            linha.append(binomio(j,k))
        pascal.append(linha)
    print (pascal)
        

def binomio (n, k):
    nfat = kfat = nkfat = 1
    for i in range (2, n+1):
        nfat *= i
        if i <= k:
            kfat *= i
        if i < n - k + 1:
            nkfat *= i
    bin = (nfat)/(kfat*nkfat)
    return bin
main ()
