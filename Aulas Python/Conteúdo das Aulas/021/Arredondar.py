"""
Faça um Programa que peça um número e
informe se o número é inteiro ou decimal. Se o número for decimal,
arredonde o número
0.4 = 3.4 - 3
"""
num = float(input("Digite um número: "))

if num != int(num):
    decimal = num - int(num)
    arredondado = int(num)

    if decimal >= 0.5:
        arredondado += 1
        
    print(num, "é decimal")
    print("Arredondando:", arredondado)
else:
    print(num, "é inteiro")
