"""
Dados n e n seqüências de números inteiros não-nulos,
cada qual seguida por um 0,
calcular a soma dos números pares de cada seqüência.
"""

n = int(input("Digite o número de sequências: "))
for cont in range(n):
    n2 = int(input("Digite o tamanho dessa sequência: "))
    soma = 0
    for cont2 in range(n2):
        num = int(input("Digite um número da sequência: "))
        if num % 2 == 0:
            soma += num
    print ("A soma dessa sequência é", soma)
    cont += 1
