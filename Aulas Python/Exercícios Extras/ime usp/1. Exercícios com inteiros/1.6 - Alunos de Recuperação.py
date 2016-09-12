"""
Dados o número n de alunos de uma turma de Introdução aos Autômatos a Pilha
(MAC 414) e suas notas da primeira prova,
determinar a maior e a menor nota obtidas por essa turma
(Nota máxima = 100 e nota mínima = 0).
"""

n = int(input("Digite n: "))
cont = 0
deRec = 0

while cont < n:
    nota = int(input("Digite uma nota: "))
    if nota >= 30 and nota < 50:
        deRec = deRec + 1
    cont = cont + 1
print ("Quantidade de alunos de recuperação: ", deRec)
