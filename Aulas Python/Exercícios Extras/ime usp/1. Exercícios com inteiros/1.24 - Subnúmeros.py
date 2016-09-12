"""
São dados dois números inteiros positivos p e q,
sendo que o número de dígitos de p é menor ou igual ao número de dígitos de q.
Verificar se p é um subnúmero de q.

Exemplos:
p = 23, q = 57238, p é subnúmero de q.
p = 23, q = 258347, p não é subnúmero de q.
"""

p = int(input("Digite p: "))
q = int(input("Digite q: "))

aux1, aux2, cont = p, q, 0
while aux1 != 0:
    aux1 //= 10
    cont += 1
while aux2 >= p:
    dig = aux2 % 10**(cont)
    if dig == p:
        print (p, "é subnúmero de", q)
        aux2 = -1
    aux2 //= 10
if aux2 != -1:
    print (p, "não é subnúmero de", q)
