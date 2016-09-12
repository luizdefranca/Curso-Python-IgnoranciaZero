"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if c < b < a:
    print(c, "<", b, "<", a)
elif c < a < b:
    print(c, "<", a, "<", b)
elif b < c < a:
    print(b, "<", c, "<", a)
elif b < a < c:
    print(b, "<", a, "<", c)
elif a < c < b:
    print(a, "<", c, "<", b)
else:
    print(a, "<", b, "<", c)
