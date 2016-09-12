lista = []
n = int(input("Digite o número de lançamentos: "))
for i in range (n):
    res = int(input("Digite o resultado do lançamento %d de %d: "%(i+1, n)))
    lista.append(res)
for i in range (1,7):
    freq = 0
    for j in range (n):
        if lista[j] == i:
            freq += 1
    print("A frequência de %d foi %d"%(i, freq))
