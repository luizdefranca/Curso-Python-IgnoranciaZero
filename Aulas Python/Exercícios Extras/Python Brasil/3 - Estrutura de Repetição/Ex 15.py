"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

n = int(input("Digite n: "))
A, B, cont = 1, 1, 2
print(A)
while cont < n:
    print(B)
    C = A + B
    A = B
    B = C
    cont += 1
print(C)
    
