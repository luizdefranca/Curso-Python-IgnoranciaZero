"""
Escreva um simples programa que receba
uma palavra e forneça todas as permutações
possíveis da palavra.
Faça isso a partir de expressões
geradoras
"""

palavra = input("Digite a palavra que você deseja permutar\n")

#Obtemos as permutações a partir do seguinte algoritmo
permutações = (palavra[i:].lower() + palavra[:i].lower() for i in range(len(palavra)))

#Agora precisamos eliminar as permutações repetidas
lista = []
for perm in permutações:
    if perm not in lista:
        lista.append(perm)

#E por último imprimimos a lista
print(lista)


