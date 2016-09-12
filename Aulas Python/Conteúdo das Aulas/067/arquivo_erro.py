
try:
    a = open('arquivo.txt', 'r')
    linha = a.readline()
    linha.split('!')
    linha = linha[0]
    a.close()
    a = open('arquivo.txt', 'a')
    a.write(linha)
except FileNotFoundError:
    print('Deu erro!')
    a = open('arquivo.txt', 'w')
    a.write('ERRO!!!!!')
finally:
    a.close()
