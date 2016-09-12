"""
Arquivo para isalpha(), islower() e isupper()

Escreva três funções: Uma que verifica se todas os chars de uma string
são letras, outra que verifica se todos os digitos de uma string sao
minusculos e outra que verifica se todos os digitos de uma string sao
maiusculos
"""
def isalpha(string):
    ehLetra = True
    for char in string:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
            ehLetra = False
            break

    return ehLetra

def islower(string):
    sim = True
    for char in string:
        if isalpha(char) and not 'a' <= char <= 'z':
            sim = False
            break

    return sim

def isupper(string):
    sim = True
    for char in string:
        if isalpha(char) and not 'A' <= char <= 'Z':
            sim = False
            break

    return sim

print(isalpha('Ola juarez, que legal'))
print(isalpha('ola'))
print()
print(islower('Pedro e Maria'))
print(islower('pedro e maria'))
print()
print(isupper('Pedro e Maria'))
print(isupper('PEDRO E MARIA'))
