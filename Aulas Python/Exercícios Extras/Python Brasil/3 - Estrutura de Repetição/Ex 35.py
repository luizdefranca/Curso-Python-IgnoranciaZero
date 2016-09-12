"""
35.	Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números
primos existentes entre 1 e um número inteiro informado pelo usuário.
"""
        
N = int(input("Digite o valor de N: "))
div = 0
for i in range(1, N+1):
    primo = True

    j = 2
    while j < i and primo:
        div += 1
        if i % j == 0:
            primo = False
        j += 1

    if primo:
        print(i)

print("Fiz %i divisões"%div)

div = 0
for i in range(1, N+1):
    primo = True

    for j in range(2, i):
        div += 1
        if i % j == 0:
            primo = False

    if primo:
        print(i)

print("Fiz %i divisões"%div)
