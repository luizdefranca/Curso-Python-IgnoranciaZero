"""
23.	Faça um Programa que peça um número e
informe se o número é inteiro ou decimal.
"""

num = float(input("Digite um número: "))

if num - int(num) == 0:
    print("O número é inteiro.")
else:
    print("O numéro é decimal.")
