"""
Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e
[76-100].
A entrada de dados deverá terminar quando for lido um número negativo.
"""

n = int(input("Digite um numero: "))

entre0_25 = entre26_50 = entre51_75 = entre76_100 = 0

while n >= 0:
    if 0 <= n <= 25:
        entre0_25 += 1
    elif 26 <= n <= 50:
        entre26_50 += 1
    elif 51 <= n <= 75:
        entre51_75 += 1
    elif 76 <= n <= 100:
        entre76_100 += 1

    n = int(input("Digite um numero: "))

print("[0-25] = ", entre0_25)
print("[26-50] = ", entre26_50)
print("[51-75] = ", entre51_75)
print("[76-100] = ", entre76_100)
