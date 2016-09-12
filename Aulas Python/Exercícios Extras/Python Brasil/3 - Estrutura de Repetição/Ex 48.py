"""
Faça um programa que peça um numero inteiro positivo e em seguida mostre
este numero invertido.
o	Exemplo:
o	  12376489
  => 98467321
"""
n = int(input("Digite um número: "))
aux = n
reverso = 0

while aux != 0:
    reverso = reverso*10 + aux%10
    aux //= 10

print("Reverso de", n, ":")
print(reverso)
