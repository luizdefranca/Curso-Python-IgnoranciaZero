"""
Dado um inteiro não-negativo n, determinar n!
"""

n = int(input("Digite n: "))
cont = 1
prod = 1
while cont < n:
    prod = prod * (cont + 1)
    cont = cont + 1
    
print ("O valor de", n, "! é igual a:", prod)
