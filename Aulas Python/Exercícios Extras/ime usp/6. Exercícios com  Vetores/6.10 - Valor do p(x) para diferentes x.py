n = int(input("Digite o grau do polinômio: "))
poli = []
for i in range (n+1):
    a = float(input("Digite o a%d: "%(i)))
    poli.append(a)
k = int(input("Digite k: "))
for j in range (k):
    x = float(input("Digite o x%d: "%(j+1)))
    soma = 0.0
    for l in range (n+1):
        soma += poli[l]*(x**(l))
    print ("x%d = %.2f"%(j, soma))
