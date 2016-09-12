"""
Dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares.
"""

n = int(input("Digite n: "))
cont = 0
soma = 1
while cont < n:
    print (soma)
    soma = soma + 2
    cont = cont + 1
