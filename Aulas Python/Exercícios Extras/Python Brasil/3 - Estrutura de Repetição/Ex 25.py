"""
25.	Faça um programa que peça para n pessoas a sua idade, ao final o
programa devera verificar se a média de idade da turma varia entre 0 e 25,
26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
conforme a média calculada.

"""

n = int(input("Digite o número de pessoas: "))
total = 0

for i in range(n):
    total += int(input("Digite a idade da pessoa %i: "%(i+1)))

media = total/n

if 0 <= media <= 25:
    print("Turma Jovem.")
elif 26 <= media <= 60:
    print("Turma adulta.")
else:
    print("Turma idosa.")
