"""
 Dados n e uma seqüência de n números inteiros, determinar o comprimento de
 um segmento crescente de comprimento máximo.

Exemplos:
Na seqüência   5,  10,  3,  2,  4,  7,  9,  8,  5
o comprimento do segmento crescente máximo é 4.

Na seqüência   10,  8,  7,  5,  2
o comprimento de um segmento crescente máximo é 1.
"""

# 5,  10,  3,  2,  4,  7,  9,  8,  5

#ant = 5
#seg = 1
#segMAX = 1
#--------------------------------
#prox = 10
#10 > 5 --> seg + 1
#--------------------------------
#ant = 10
#prox = 3
#3 > 10 --> parou
# --> seg > segMAX --> segMAX = seg => seg = 1

#--------------------------------
#ant = 3
#prox = 2
# 2 > 3 --> parou
# --> seg > segMAX --> seg = 1

n = int(input("Digite o tamanho da sequência: "))
ant = int(input("Digite o numero 1: "))
cont = seg = segMAX = 1
while cont < n:
    prox = int(input("Digite o numero %i: "%(cont+1)))
    if prox > ant:
        seg += 1
    else:
        seg = 1
        
    if seg > segMAX:
        segMAX = seg
        
    cont += 1
    ant = prox

print("O maior segmento crescente da sequência é", segMAX)
