"""
Escreve um programa que recebe um número x e devolve o primeiro índice de
uma lista que contem o elemento x. Caso x não esteja na lista, imprima
uma mensagem adequada
"""

a = [1,2,3,4,5]

x = int(input("Digite o valor de x: "))
"""
achei = False
i = 0
while not achei and i < len(a):
    if a[i] == x:
        achei = True
        print("Elemento %i se encontra no indice %i"%(x, i))

    i+=1

if not achei:
    print("%i nao pertence a lista"%x)
"""

print(a.index(x))
    
