"""
39.	Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo representando a sua
altura em centímetros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com
suas alturas.

"""

numero_maior = numero_menor = int(input("Digite o seu número: "))
altura_maior = altura_menor = float(input("Digite sua altura: "))

for i in range(9):
    numero = int(input("Digite o seu número: "))
    altura = float(input("Digite sua altura: "))

    if altura < altura_menor:
        altura_menor = altura
        numero_menor = numero
    if altura > altura_maior:
        altura_maior = altura
        numero_maior = numero

print("O Aluno de numero %i tem a maior altura(%.2f m)"%(numero_maior, altura_maior))
print("O Aluno de numero %i tem a menor altura(%i m)"%(numero_menor, altura_menor))
