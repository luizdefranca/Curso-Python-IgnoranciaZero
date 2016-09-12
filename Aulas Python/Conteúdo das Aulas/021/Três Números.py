"""
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    a.	o produto do dobro do primeiro com metade do segundo .
    b.	a soma do triplo do primeiro com o terceiro.
    c.	o terceiro elevado ao cubo.

"""
int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))
real = float(input("Digite um número real: "))

print((2*int1)*(int2/2))
print(3*int1 + real)
print(real**3)
