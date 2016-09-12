"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
vetor = [5]
for i in range(1, 6):
    num = int(input("Digite o número %i de 5: "%i))
    vetor.append(num)

print(vetor)
