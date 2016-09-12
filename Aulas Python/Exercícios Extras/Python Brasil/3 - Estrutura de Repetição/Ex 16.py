"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.
"""

A, B, cont = 1, 1, 2
print(A)
while cont < 500:
    print(B)
    C = A + B
    A = B
    B = C
    cont += 1
print(C)
