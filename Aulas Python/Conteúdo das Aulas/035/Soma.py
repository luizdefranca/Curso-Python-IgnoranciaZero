"""
Escreva uma função que obtenha a soma de vários números de entrada
"""

def soma(num2, *lista):
    soma_num = 0

    print(lista)

    for num in lista:
        soma_num += num

    return soma_num

a = (1,2,3,4)

print(soma(1,2,3,4,5))
