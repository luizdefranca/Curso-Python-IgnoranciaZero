"""
Crie uma lista, peça para o usuário escolher um indice da lista,
imprima o elemento da lista neste indice e o remova de lista,
depois imprima a lista.
"""

a = [1,2,3,4,5]

print(a)

indice = int(input("Digite o indice(de 0 até %i) do elemento a ser removido: "%(len(a) - 1)))

"""
print("Elemento:", a[indice])

b = []

for i in range(len(a)):
    if i != indice:
        b.append(a[i])

a = b
"""
print("Elemento:", a.pop(indice))

print(a)
    
