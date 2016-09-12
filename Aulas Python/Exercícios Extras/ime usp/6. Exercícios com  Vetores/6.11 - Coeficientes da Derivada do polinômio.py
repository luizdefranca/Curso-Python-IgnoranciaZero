n = int(input("Digite o grau do polinômio: "))
poli = []
for i in range (n+1):
    a = float(input("Digite o a%d: "%(i)))
    poli.append(a)
poli_d =[]
for r in range (1, n+1):
    poli_d.append(poli[r]*r)
print(poli_d)
