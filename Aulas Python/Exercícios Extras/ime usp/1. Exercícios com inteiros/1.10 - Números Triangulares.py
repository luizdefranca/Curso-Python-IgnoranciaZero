"""
Dizemos que um número natural é triangular se ele é produto de três números
naturais consecutivos.

Exemplo: 120 é triangular, pois 4.5.6 = 120.
Dado um inteiro não-negativo n, verificar se n é triangular.
"""

n = int(input("Digite n: "))
i, j, k = 1, 2, 3
while i * j * k < n:
    i += 1
    j += 1
    k += 1
if i * j * k == n:
    print (n, "é triangular, produto de ", i, j, k)
else:
    print (n, "não é triangular.")
