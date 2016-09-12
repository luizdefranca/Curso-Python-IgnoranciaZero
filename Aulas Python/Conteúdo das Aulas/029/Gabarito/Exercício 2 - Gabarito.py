"""
Escreve um programa que recebe uma lista de números até que seja dada a entrada
-1, e depois imprima todos os números pares da sequência
"""

lista = []

i = int(input("Digite um número da lista: "))
while i != -1:
    lista.append(i)
    i = int(input("Digite um número da lista: "))

print("Os seguintes números da lista são pares: ")
for num in lista:
    if num % 2 == 0:
        print(num)
