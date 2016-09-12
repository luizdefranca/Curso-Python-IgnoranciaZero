"""
Dado um numero inteiro não-negativo n, determinar n!
5! = ((((5*4)*3)*2)*1) = 120
3! = 3*2*1 = 6
"""
n = int(input("Digite n: "))

"""
prod = n
cont = n-1
while cont > 1:
    prod = prod*cont
    cont = cont - 1
"""

prod = 1
cont = 2

while cont <= n:
    prod = prod*cont
    cont = cont + 1

print(n, "! =", prod)
