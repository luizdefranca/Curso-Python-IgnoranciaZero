"""
Dados n números inteiros positivos, calcular a soma dos que são primos. 
"""

n = int(input("Digite n: "))
cont, k, soma = 0, 2, 0
while cont < n:
    p = int(input("Digite um número da sequência: "))
    while k < p:
        if p % k == 0:
            k = p + 1
        k += 1
        if k == p:
            soma += p
    cont += 1
print ("A soma é", soma)
    
