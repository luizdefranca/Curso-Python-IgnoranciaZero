"""
Escreva um programa que crie uma lista de elementos, até se entrar -1,
e depois imprima todos os números da lista que são maiores que 10.
"""

lista = []

i = int(input("Digite um número da lista: "))
while i != -1:
    lista.append(i)
    i = int(input("Digite um número da lista: "))

print("Os seguintes números da lista são maiores do que 10")
for num in lista:
    if num > 10:
        print(num)


    
