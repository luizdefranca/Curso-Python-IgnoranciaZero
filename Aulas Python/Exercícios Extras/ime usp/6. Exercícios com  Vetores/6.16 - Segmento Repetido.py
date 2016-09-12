k = int(input("Digite k: "))
lista = []
for i in range (k):
    ele = int(input("Digite o número %d de %d: "%(i+1, k)))
    lista.append(ele)
m = 1
resp = True
for p in range (k - 1, 0, -2):
    for i in range (p):
        cont = 0
        for z in range (m):       
            if lista [i + z] == lista [i + m + z]:
                resp = True
                cont += 1
            else:
                resp = False
        if resp == True and cont == m:
            print ("Para i = %d e m = %d temos uma repetição."%(i,m))
    m += 1

p #número de testes
m #tamanho do segmento
i #elemento de teste
