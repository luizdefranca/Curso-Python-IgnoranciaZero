"""
Calcule n! usando o for loop
5! = 5X4X3X2X1 = 120
"""
n = int(input("Digite o valor de n: "))
fatorial = 1

"""for fator in range(2, n+1):
    fatorial *= fator"""

for fator in range(n, 1, -1):
    fatorial *= fator

print("%i! é igual a %i"%(n, fatorial))
