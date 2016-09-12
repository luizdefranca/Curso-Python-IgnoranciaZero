"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver
um programa que leia um conjunto indeterminado de temperaturas, e informe
ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.

7, 5, 3524, 5, 5, 7, 67, 2, 78
"""
num = int(input("Digite o número de temperaturas registradas: "))

soma = maior = menor = float(input("Digite a temperatura 1: "))

for i in range(2, num+1):
    temp = float(input("Digite a temperatura %d: "%i))

    if temp > maior:
        maior = temp

    if temp < menor:
        menor = temp

    soma += temp

print("A maior temperatura é %6.2f ºC"%maior)
print("A menor temperatura é %6.2f ºC"%menor)
print("A média das temperaturas é %6.2f ºC"%(soma/num))
