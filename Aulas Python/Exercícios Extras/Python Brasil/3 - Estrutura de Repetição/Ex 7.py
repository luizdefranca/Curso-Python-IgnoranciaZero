"""
Faça um programa que leia 5 números e informe o maior número.
"""

cont = 2
maior = int(input("Informe o numero 1: "))
while cont <= 5:
    num = int(input("Informe o numero %i: " %cont))
    if num > maior:
        maior = num

    cont += 1

print("O maior numero é", maior)
