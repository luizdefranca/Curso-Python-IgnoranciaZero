"""
Dados um inteiro x e um inteiro não-negativo n, calcular x n. 
"""

base = int(input("Base: "))
exp = int(input("Expoente: "))
cont = 0
prod = 1
if exp < 0:
    while cont > exp:
        cont = cont - 1
        prod = prod * 1/base
else:
    while cont < exp:
        cont = cont + 1
        prod = prod * base

print (base, "elevado à", exp, "é igual a", prod)
