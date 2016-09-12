"""
33.	O Departamento Estadual de Meteorologia lhe contratou para desenvolver
um programa que leia as um conjunto indeterminado de temperaturas, e informe
ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.

"""

n = int(input("Digite o número de temperaturas registradas: "))
maior = menor = total = float(input("Digite a temperatura 1: "))
for i in range (2, n+1):
    temp = float(input("Digite a temperatura %i: "%i))
    total += temp

    if temp > maior:
        maior = temp
    if temp < menor:
        menor = temp

print("Maior Temperatura Registrada: %g"%maior)
print("Menor Temperatura Registrada: %g"%menor)
print("Média das Temperaturas Registradas: %g"%(total/n))
