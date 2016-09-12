"""
Dados n e n seqüências de números inteiros não-nulos,
cada qual seguida por um 0,
calcular a soma dos números pares de cada seqüência.
"""
n = int(input("Digite o número de sequências: "))
print("")
for i in range(n):
    print("Sequência %i:"%(i+1))
    num = int(input("Digite um numero da sequência: "))
    soma = 0
    while num != 0:
        if num % 2 == 0:
            soma += num
        num = int(input("Digite um numero da sequência: "))

    print("A soma da sequência %i é %i"%(i+1, soma))
    print("")
