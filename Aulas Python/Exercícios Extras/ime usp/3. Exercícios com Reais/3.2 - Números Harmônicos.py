n = int(input("Digite n: "))
soma = 0.0
for i in range (n):
    k = float(input("Digite o %d número: "%(i+1)))
    num = 1/k
    soma += num
print ("O número harmônico é %.2f"%(soma))
