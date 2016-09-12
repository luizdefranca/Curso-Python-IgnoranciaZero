"""
Faça um programa que peça 10 números inteiros, calcule e
mostre a quantidade de números pares e a quantidade de números impares.
"""

cont = 1
par = 0
impar = 0
while cont <= 10:
    num = int(input("Digite o numero %i: "%cont))
    if num % 2 ==0:
        par += 1
    else:
        impar += 1

    cont += 1

print("Há um total de %i numeros pares e %i numeros impares."%(par, impar))
