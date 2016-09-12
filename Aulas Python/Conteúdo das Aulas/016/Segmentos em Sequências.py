"""
Dados n e uma seqüência de n números inteiros, determinar quantos segmentos
de números iguais consecutivos compõem essa seqüência.

Exemplo: A seguinte seqüência é formada por 5 segmentos de números iguais:
5,  2,  2,  3,  4,  4,  4,  4,  1,  1 
"""

#ant = 5
#seg = 1
#n = 10
#cont = 0
#-----------------------------------------
#prox = 2
#ant == prox -->
#ant != prox --> seg += 1
#ant = prox = 2
#--------------------------------------
#ant = 2
#prox = 2
#ant == prox
#ant = prox
#-------------------------------------

n = int(input("Digite o tamanho da sequência: "))

ant = int(input("Digite o numero 1: "))
cont = seg = 1

while cont < n:
    prox = int(input("Digite o numero %i: "%(cont + 1)))
    if prox != ant:
        seg += 1
    ant = prox
    cont += 1

print("A sequência tem %i segmentos"%seg)
