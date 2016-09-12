"""
Faça um Programa que leia três números e mostre o maior deles
"""

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

print("O maior número é:")
############################################
#Algoritmo para a aula 009
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
#############################################
#Algoritmo para a aula 010
if a > b > c:
    print(a)
elif a > c > b:
    print(a)
elif b > a > c:
    print(b)
elif b > c > a:
    print(b)
elif c > a > b:
    print(c)
else:
    print(c)
