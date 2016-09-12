def main ():
    n = int(input("Digite n: "))
    seq1 = f(n)
    seq2 = f(n)
    total = seq1 + seq2
    lista = []
    while total != 0:
        dig = total%10
        lista.append(dig)
        total //= 10
    lista2 = []
    for i in range (len(lista) - 1, -1, -1):
        lista2.append(lista[i])
    print (lista2)
def f (n):
    seq = 0
    for i in range (1, n+1):
        ele = float(input("Digite o elemento %d de %d: "%(i, n)))
        seq += ele*(10**(n-i))
    return seq

main ()
