"""
Modifique o simulador de megasena de forma que agora também seja contabilizado
quando se ganha quinas e quadras
"""
import random

n = int(input("Digite o número de testes: "))
soma = soma_quina = soma_quadra = 0
megasena = list(range(1,61))
meu = [6, 13, 25, 33, 42, 50]

for i in range(n):
    sorteado = []

    cont = cont_quina = cont_quadra = 0

    while sorteado != meu:
        cont += 1

        sorteado = []

        mega_copy = megasena.copy()

        for j in range(6):
            ele_sort = random.choice(mega_copy)
            sorteado.append(ele_sort)
            mega_copy.remove(ele_sort)

        sorteado.sort()

        iguais = 0

        for k in range(len(sorteado)):
            if sorteado[k] == meu[k]:
                iguais += 1

        if iguais == 4:
            cont_quadra += 1
        elif iguais == 5:
            cont_quina += 1

    soma += cont
    soma_quina += cont_quina
    soma_quadra += cont_quadra

    print("Resultado do teste %i: %i"%(i+1,cont))
    print("Quinas:", cont_quina)
    print("Quadra:", cont_quadra)

soma /= n
soma_quina /= n
soma_quadra /= n
print("A média artimética das quadras do teste foi", soma_quadra)
print("A média artimética das quinas do teste foi", soma_quina)
print("A média artimética do teste foi", soma)
