"""
Dado um inteiro positivo n, verificar se n é primo.
"""

p = int(input("Digite p: "))
k = 2
while k < p:
    if p % k == 0:
        print (p, "não é primo.")
        k = p
    k += 1
if k == p:
    print (p, "é primo.")
            
