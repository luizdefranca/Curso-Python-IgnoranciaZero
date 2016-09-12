"""
sys
    argv = devolve os argumentos colocados na linha de comando

Flags --> -l 14 = Define o número de linhas a ser lido por iteração
"""

import sys

print(sys.argv)


def mais(text, numlinhas=15):
    linhas = text.splitlines()
    
    while linhas:
        chunk = linhas[:numlinhas]
        linhas = linhas[numlinhas:]
        for linha in chunk: print(linha)
        if linhas and input('Mais?') not in ['s', 'S']: break

if __name__ == '__main__':
    arq, numlinhas = "", 15
    if len(sys.argv) > 1:
        arq = open(sys.argv[1]).read()
    if len(sys.argv) > 2:
        if '-l' in sys.argv:
            numlinhas = int(sys.argv[sys.argv.index('-l') + 1])

    mais(arq, numlinhas)    

