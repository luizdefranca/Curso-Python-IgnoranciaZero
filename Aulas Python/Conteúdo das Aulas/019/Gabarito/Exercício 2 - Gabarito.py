"""
Dados dois números inteiros positivos i e j diferentes de 0,
imprimir todos os divisores comuns de i e j.

Exemplo: i = 2 e j = 3 a saída deverá ser : 1
i = 9, j = 21 a saída deverá ser: 1, 3
"""

i = int(input("Digite o valor de i: "))
j = int(input("Digite o valor de j: "))

print("Os divisores comuns de %i e %d são: "%(i, j))
print(1)
divisor = 2
while divisor <= i and divisor <= j:
    if i % divisor == 0 and j % divisor == 0:
        print(divisor)
    divisor += 1
