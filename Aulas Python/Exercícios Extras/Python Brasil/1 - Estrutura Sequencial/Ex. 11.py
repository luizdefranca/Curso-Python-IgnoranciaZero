"""
11.	Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    a.	o produto do dobro do primeiro com metade do segundo .
    b.	a soma do triplo do primeiro com o terceiro.
    c.	o terceiro elevado ao cubo.

"""

int1 = int(input("Digite o primeiro numero inteiro: "))
int2 = int(input("Digite o segundo numero inteiro: "))
real = float(input("Digite o numero real: "))

#A
print("Letra A:", 2*int1*int2/2)

#B
print("Letra B:", 3*int1 + real)

#C
print("Letra C:", real**3)
