"""
Dado um número natural na base decimal, transformá-lo para a base binária.

Exemplo: Dado 18 a saída deverá ser 10010. 
"""

n = int(input("Digite um número: "))
cont, final = 0, 0
aux = n
while aux > 0:
    dig = aux % 2
    aux = aux // 2
    if dig != 0:
        final = final + 10**cont
    cont += 1
print ("O número", n, "é igual a", final)
