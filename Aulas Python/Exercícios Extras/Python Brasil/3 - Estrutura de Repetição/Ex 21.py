"""
Faça um programa que peça um número inteiro e determine se ele é ou não
um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

p = int(input("Digite p: "))
k = 2
while k < p:
    if p % k == 0:
        print (p, "não é primo.")
        k = p
    k += 1

if k == p:
    print (p, "é primo.")

if p == 1:
    print (p, "é primo.")
            
