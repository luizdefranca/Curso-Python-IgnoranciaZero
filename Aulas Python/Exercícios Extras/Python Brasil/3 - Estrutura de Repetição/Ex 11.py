"""
Altere o programa anterior para mostrar no final a soma dos números.
"""
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

cont = menor+1
soma = 0

while cont < maior:
    print(cont)
    soma += cont
    cont += 1

print("Soma:",soma)
