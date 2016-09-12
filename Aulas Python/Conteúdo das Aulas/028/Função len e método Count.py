"""
Recebendo entradas inteiras do usuário que só devem ser interrompidas com a
entrada do número -1, e recebendo um elemento qualquer, calcular o número
de vezes que esse elemento aparece na sequência digitada pelo usuário
"""

lista = []

num = int(input("Digite um número da sequência: "))

while num != -1:
    lista.append(num)
    num = int(input("Digite um número da sequência: "))

elemento = int(input("Digite o elemento a ser procurado: "))

"""
cont = 0

for i in range(len(lista)):
    if lista[i] == elemento:
        cont += 1
"""

print("O elemento %i aparece %i vezes na sequência."%(elemento, lista.count(elemento)))
        
    
