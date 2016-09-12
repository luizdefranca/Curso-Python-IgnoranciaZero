"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num
vetor a média de cada aluno, imprima o número de alunos com média maior ou
igual a 7.0.
"""
ALUNOS = 10

medias = []

for i in range(1, ALUNOS+1):
    notas = 0
    for j in range(1, 5):
        notas += float(input("Digite a nota %i de 4 do aluno %i de %i: "%(j,i,ALUNOS)))

    notas /= 4

    medias.append(notas)

num = 0

for media in medias:
    if media >= 7.0:
        num += 1

print("O número de alunos com média maior do que 7.0 é", num)
