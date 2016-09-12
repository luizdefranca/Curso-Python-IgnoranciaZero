"""
Arquivo para count

Escreva a seguinte função:
1. Conte o número de ocorrências de uma substring em uma string
"""
def count(frase, sub):
    cont = 0

    for i in range(len(frase) + 1 - len(sub)):
        if frase[i:i+len(sub)] == sub:
            cont += 1

    return cont

print(count('mississippi', 'ss'))
