"""
Escreva um programa em que dado a posição i e um número qualquer x,
deve-se inserir esse elemento numa lista na posição determinada

Exemplo:
lista = [1,2,3,4]
Digite a posição: 2
Digite o elemento: 8000
lista = [1,2,8000,3,4]
"""

a = [1,2,3,4]

print("lista =", a)

pos = int(input("Digite a posição: "))
ele = int(input("Digite o elemento: "))
"""
b = []

for i in range(len(a)):
    if i == pos:
        b.append(ele)

    b.append(a[i])
a = b
"""
a.insert(pos,ele)

print("lista =", a)
