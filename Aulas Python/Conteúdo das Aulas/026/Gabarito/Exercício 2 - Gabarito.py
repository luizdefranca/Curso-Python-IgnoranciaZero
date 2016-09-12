"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os dois vetores.
"""

PAR = []
IMPAR = []

for i in range(1, 21):
    num = int(input("Digite o número %i de 20: "%i))

    if num%2 == 0:
        PAR.append(num)
    else:
        IMPAR.append(num)

print("Pares: ", PAR)
print("Impares: ", IMPAR)
