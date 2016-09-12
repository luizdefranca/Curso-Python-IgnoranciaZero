"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
armazene os resultados em um vetor. Depois, mostre quantas vezes cada valor
foi conseguido.
"""
import random
vetor = []

n = int(input("Digite o número de lançamentos: "))
for i in range(n):
    vetor.append(random.randint(1,6))

for i in range(1, 7):
    print("A face %i apareceu %.2f%% vezes."%(i, 100*vetor.count(i)/n))
