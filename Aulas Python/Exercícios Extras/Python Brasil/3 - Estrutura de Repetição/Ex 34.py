"""
Os números primos possuem várias aplicações dentro da Computação,
por exemplo na Criptografia. Um número primo é aquele que é divisível
apenas por um e por ele mesmo.
Faça um programa que peça um número inteiro e determine se ele é ou não
um número primo.
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
