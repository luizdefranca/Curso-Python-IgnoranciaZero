"""
Dados n e uma seqüência de n números inteiros,
determinar a soma dos números pares.
"""

n = int(input("Digite n: "))
cont = 0
soma = 0

while cont < n:
    num = int(input("Digite um número: "))
    if num%2 == 0:
        soma += num
    cont += 1

print (soma)
