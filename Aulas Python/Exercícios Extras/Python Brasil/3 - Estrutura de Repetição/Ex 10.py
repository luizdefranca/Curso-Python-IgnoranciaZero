"""
Faça um programa que receba dois números inteiros
e gere os números inteiros que estão no intervalo compreendido por eles.
"""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

cont = menor+1

while cont < maior:
    print(cont)
    cont += 1
