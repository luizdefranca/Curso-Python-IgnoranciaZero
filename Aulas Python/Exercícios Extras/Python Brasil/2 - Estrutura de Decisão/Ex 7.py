"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a > b > c:
    print("Maior: ",a, "\nMenor: ", c)
elif a > c > b:
    print("Maior: ",a, "\nMenor: ", b)
elif b > a > c:
    print("Maior: ",b, "\nMenor: ", c)
elif b > c > a:
    print("Maior: ",b, "\nMenor: ", a)
elif c > a > b:
    print("Maior: ",c, "\nMenor: ", b)
else:
    print("Maior: ",c, "\nMenor: ", a)
