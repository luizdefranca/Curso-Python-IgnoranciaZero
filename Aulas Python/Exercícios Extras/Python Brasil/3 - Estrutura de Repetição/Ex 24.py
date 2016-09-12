"""
24.	Faça um programa que calcule o mostre a média aritmética de N notas.
"""
N = int(input("Digite o valor de N: "))

total = 0
for i in range(N):
    total += float(input("Digite a nota %i: "%(i+1)))

print("A média das notas é %g"%(total/N))
