"""
Dado um número inteiro positivo, determine a sua decomposição em
fatores primos calculando também a multiplicidade de cada fator. 
"""

n = int(input("Digite um número: "))
fator, mult = 2, 0
while n > 1:
    while n % fator == 0:
        mult += 1
        n = n / fator
    if mult > 0:
        print ("O fator", fator, "tem multiplicidade", mult)
        mult = 0
    fator += 1
