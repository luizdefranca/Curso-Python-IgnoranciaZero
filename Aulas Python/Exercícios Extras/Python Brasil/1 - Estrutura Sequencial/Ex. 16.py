"""
Faça um programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta a
serem compradas e o preço total.
"""

area = int(input("Digite o tamanho da área a ser pintada: "))

litros = area//3

if area % 3 > 0:
    litros += 1

quantidade = litros//18

if litros % 18 > 0:
    quantidade += 1

print("Serão necessárias", quantidade, "latas de tinta.")
print("Será gasto no total R$", quantidade*80)
