"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

idades = []
alturas = []

for i in range(1, 6):
    idade = int(input("Digite a idade da pessoa %i de 5: "%i))
    altura = float(input("Digite a altura(m) da pessoa %i de 5: "%i))

    idades.append(idade)
    alturas.append(altura)




#Usando slice
"""
idades_invertida = idades[::-1]
alturas_invertida = alturas[::-1]

for i in range(5):
    print("Idade %i: %i"%(5 - i, idades_invertida[i]))
    print("Altura %i: %.2f"%(5 - i, alturas_invertida[i]))
"""



#Usando range
"""
for i in range(4, -1, -1):
    print("Idade %i: %i"%(i+1, idades[i]))
    print("Altura %i: %.2f"%(i+1, alturas[i]))
"""


#usando reverse
"""
idades.reverse()
alturas.reverse()
for i in range(5):
    print("Idade %i: %i"%(5 - i, idades[i]))
    print("Altura %i: %.2f"%(5 - i, alturas[i]))
"""

