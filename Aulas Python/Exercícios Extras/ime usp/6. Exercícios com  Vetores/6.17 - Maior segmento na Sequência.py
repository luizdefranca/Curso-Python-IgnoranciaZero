k = int(input("Digite k: "))
lista = []
for i in range (k):
    ele = int(input("Digite o número %d de %d: "%(i+1, k)))
    lista.append(ele)
seg2 = 0
for i in range (k):
    seg1 = lista [i]
    p = k - i - 1
    for n in range (1, p + 1):
        seg1 += lista [i + n]
        if seg1 > seg2:
            seg2 = seg1
print ("A soma do maior segmento é: ", seg2)
