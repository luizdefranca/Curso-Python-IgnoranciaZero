"""
Arquivo para replace

Escreva uma função que recebe uma string, uma substring velha, e uma substring
nova e devolve uma copia da string com todas as substrings velha substituidas
pela subtring nova
"""

def replace(frase, velha, nova):
    palavra = ''
    i = 0

    while i < len(frase) + 1 - len(velha):
        if frase[i:i+len(velha)] != velha:
            palavra += frase[i]
        else:
            i += len(velha)
            palavra += nova
            continue

        i+= 1

    palavra += frase[i:]

    return palavra

print(replace('mississippi', 'ss', 'zzz'))
