"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000
"""

n = int(input("Digite o tamanho da sequência: "))

ok = False
while ok != True:
    menor = maior = int(input("Digite o numero 1 da sequência: "))
    if 0 < maior < 1000:
        ok = True
    else:
        print("Entrada invalida, digite um numero entre 0 e 1000")

cont = 2

soma = maior

while cont <= n:

    ok = False
    while ok != True:
        num = int(input("Digite o numero %i da sequência: "%cont))
        if 0 < num < 1000:
            ok = True
        else:
            print("Entrada invalida, digite um numero entre 0 e 1000")

    if num > maior:
        maior = num
    if num < menor:
        menor = num

    soma += num

    cont += 1

print("A soma é %i, com maior número %i e menor %i" %(soma, maior, menor))
