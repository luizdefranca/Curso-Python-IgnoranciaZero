"""
Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.
"""
n = int(input("Digite o tamanho da sequência: "))

menor = maior = int(input("Digite o numero 1 da sequência: "))

cont = 2

soma = maior

while cont <= n:
    num = int(input("Digite o numero %i da sequência: "%cont))
    if num > maior:
        maior = num
    if num < menor:
        menor = num

    soma += num

    cont += 1

print("A soma é %i, com maior número %i e menor %i" %(soma, maior, menor))
    
