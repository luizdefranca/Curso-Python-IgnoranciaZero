"""
Dados n e uma seqüência de n números inteiros, determinar quantos segmentos
de números iguais consecutivos compõem essa seqüência.

Exemplo: A seguinte seqüência é formada por 5 segmentos de números iguais:
5,  2,  2,  3,  4,  4,  4,  4,  1,  1 
"""

n = int(input("Digite o tamanho da sequência: "))
cont, seq = 1, 1
ant = int(input("Digite um número da sequência: "))
while cont < n:
    num = int(input("Digite um número da sequência: "))
    if num != ant:
        seq += 1
    ant = num
    cont += 1
print ("O número de segmentos é ", seq)
