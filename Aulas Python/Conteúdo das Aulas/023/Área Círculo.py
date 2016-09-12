"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
from math import pi

raio = float(input("Digite o raio do círculo: "))

area = pi*raio*raio

print("A área do círculo de raio %.10g é %.10g"%(raio, area))
