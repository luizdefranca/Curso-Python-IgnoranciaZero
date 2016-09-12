"""
Arquivo para os métodos find e index

Escreva uma função que receba um string e uma sub
string e verifique se a substring faz parte da string
"""

def find(frase, sub):
    for i in range(len(frase) + 1 - len(sub)):
        if frase[i:i+len(sub)] == sub:
            return i

    return -1

def index(frase, sub):
    for i in range(len(frase) + 1 - len(sub)):
        if frase[i:i+len(sub)] == sub:
            return i

    return 'ERRO'
    
print(find('mississippi', 'ss'))
print(index('mississippi', 'a'))
