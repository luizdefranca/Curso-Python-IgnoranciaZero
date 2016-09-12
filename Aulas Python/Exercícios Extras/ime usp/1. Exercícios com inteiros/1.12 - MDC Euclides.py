"""
Dados dois números inteiros positivos, determinar o máximo divisor comum
entre eles usando o algoritmo de Euclides.
"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
r = n1 % n2
while r != 0:
    n1 = n2
    n2 = r
    r = n1 % n2
print ("O m.d.c é", n2)
