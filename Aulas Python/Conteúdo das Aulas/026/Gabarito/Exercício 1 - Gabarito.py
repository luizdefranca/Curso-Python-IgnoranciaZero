"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = []

soma = 0

for i in range(1, 5):
    nota = float(input("Digite a nota %i de 4: "%i))
    notas.append(nota)
    soma += nota

for i in range(4):
    print("Nota %i: %i"%(i+1, notas[i]))

print("A média é %.3g"%(soma/4))
