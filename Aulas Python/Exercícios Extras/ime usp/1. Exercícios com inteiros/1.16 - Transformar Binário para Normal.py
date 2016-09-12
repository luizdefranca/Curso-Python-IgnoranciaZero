"""
Dado um número natural na base binária, transformá-lo para a base decimal.

Exemplo:
Dado 10010 a saída será 18, pois
1 * (2**4) + 0*(2**3) + 0*(2**2) + 1*(2**1) + 0*(2**0) = 18. 
"""

n = int(input("Digite um número binário: "))
cont, soma = 0, 0
aux = n
while aux > 0:
    dig = aux % 10
    aux = aux // 10
    soma = soma + dig * 2**cont
    cont += 1
print ("O número", n, "equivale a", soma)
