n = int(input("Digite n: "))
lista = []
for i in range (n):
    num = float(input("Digite o número %d de %d: "%(i+1,n)))
    lista.append(num)
for i in range (n-1, -1, -1):
    print(lista[i])
