"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número
inteiro fornecido pelo usuário. O programa deverá mostrar também o número de
divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões)
executados.
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
