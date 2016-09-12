"""
Arquivo para startswith

Escreva uma função que verififica se uma determinada string começa
com uma determinada substring
"""

def startswith(string, sub):
    return string[:len(sub)] == sub

print(startswith('Sim', 'S'))
print(startswith('Sim', 's'))
print(startswith('Sim', 'Si'))
