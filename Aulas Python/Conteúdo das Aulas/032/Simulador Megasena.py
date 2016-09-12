"""
No site da megasena está escrito que a chance de um jogador ganhar
é de 1 em 50.063.860. Escreva um programa usando o módulo random e os conceitos
utilizados em aula para testar essa probabilidade.
"""
import random

meu = [6, 13, 25, 33, 42, 50]

megasena = list(range(1,61))

n = int(input("Número de testes: "))

soma = 0

for i in range(n):
    sorteado = []

    cont = 0

    while meu != sorteado:
        mega_sort = megasena.copy()

        sorteado = []

        for j in range(6):
            num_sorteado = random.choice(mega_sort)
            sorteado.append(num_sorteado)
            mega_sort.remove(num_sorteado)

        sorteado.sort()

        cont += 1

    soma += cont

    print("Resultado do teste %i: %i tentativas"%(i+1, cont))

soma /= n

print("Média dos resultados:", soma)

        
