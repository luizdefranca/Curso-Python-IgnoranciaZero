n = int(input("Digite n: "))
lista = []
for i in range (n):
    ele = float(input("Digite o elemento %d de %d: "%(i+1, n)))
    lista.append(ele)
for j in range (n):
    freq = 0
    for k in range (n):
        if lista[j] == lista[k]:
            freq += 1
    print ("O elemento %.1f aparece %d vezes"%(lista[j], freq))
