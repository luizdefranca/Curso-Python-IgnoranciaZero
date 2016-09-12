"""
Dizemos que um número i é congruente módulo m a j se i % m = j % m. 
 
    Exemplo: 35 é congruente módulo 4 a 39, pois
    35 % 4 = 3 = 39 % 4.

Dados inteiros positivos n, j e m, imprimir os
n primeiros naturais congruentes a j módulo m.
"""

n = int(input("Digite n: "))
j = int(input("Digite j(o número a ser divido): "))
m = int(input("Digite m(divisor): "))
cont, test = 0, 1
while cont < n:
    if test % m == j % m:
        print (test)
        cont += 1
    test += 1
