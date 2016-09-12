"""
27.	Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.

"""

turmas = int(input("Digite o número de turmas: "))
total = 0
for i in range(turmas):
    alunos = int(input("Digite o número de alunos da turma %i: "%(i+1)))
    while alunos > 40 and alunos < 0:
        print("Numero de alunos inválido, digite novamente.")
        alunos = int(input("Digite o número de alunos da turma %i: "%(i+1)))

    total += alunos

print("Há uma média de %g alunos por turma."%(total/turmas))
