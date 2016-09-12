"""
Um matemático italiano da idade média conseguiu modelar o ritmo de crescimento
da população de coelhos (1) através de uma seqüência de números naturais que
passou a ser conhecida como seqüência de Fibonacci (2).

O n-ésimo número da seqüência de Fibonacci Fn
é dado pela seguinte fórmula de recorrência:

F1 = 1
F2 = 1
Fi = F(i-1) + F(i-2) para i >= 3

Faça um programa que, dado n, calcula Fn. 
"""

n = int(input("Digite n: "))
A, B, cont = 1, 1, 2
while cont < n:
    C = A + B
    A = B
    B = C
    cont += 1
print ("O número", n, "da sequência de Fibonocci é", C)
    
