import sys
linhas = sys.stdin.readlines()
linhas.sort()
for linha in linhas: print(linha, end='')
