"""
Dados um inteiro positivo n e uma seqüência de n inteiros positivos,
determinar o máximo divisor comum a todos eles.
"""

n = int(input("Digite n: "))
cont = 1
ant = int(input("Digite um número: "))
while cont < n:
    num = int(input("Digite um número: "))
    r = num % ant
    while r != 0:
        num = ant
        ant = r
        r = num % ant
    cont += 1
print ("O m.d.c é", ant)
