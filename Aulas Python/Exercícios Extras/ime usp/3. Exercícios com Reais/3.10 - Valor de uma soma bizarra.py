n = float(input("Digite n: "))
soma = n
termo, i = 1/n, 1
while termo != n:
    soma += termo
    termo = (i+1)/(n-i)
    i += 1
print ("%.2f"%(soma))
