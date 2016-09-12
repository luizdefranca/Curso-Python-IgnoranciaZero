"""
28.	Faça um programa que calcule o valor total investido por um colecionador
em sua coleção de CDs e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.

"""

cds = int(input("Digite o número de cds: "))

total = 0

for i in range(cds):
    total += float(input("Digite o total gasto no CD %i: "%(i+1)))

print("Total gasto: R$", total)
print("Média gasta por CD: R$",(total/cds))
