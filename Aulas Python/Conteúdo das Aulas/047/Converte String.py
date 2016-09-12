"""
Faça dois funções: Uma que coloque uma string em maiusculo e outra
que coloque uma str em minusculo
"""
def main():
    string = 'CHiCleTe'

    print(tudoMinusculo(string))
    print(tudoMaiusculo(string))

def tudoMinusculo(string):
    minusculo = ""

    for char in string:
        if 'A' <= char <= 'Z':
            char = chr(ord(char) + (ord('a') - ord('A')))
        minusculo += char

    return minusculo

def tudoMaiusculo(string):
    miausculo = ""

    for char in string:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - (ord('a') - ord('A')))
        miausculo += char

    return miausculo

main()

