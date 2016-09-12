"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120
"""

n = int(input("Digite n: "))
cont = 1
prod = 1
while cont < n:
    prod = prod * (cont + 1)
    cont = cont + 1
    
print ("O valor de", n, "! é igual a:", prod)
