"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a
quantidade de centenas, dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre
outros. Exemplo:
o	326 = 3 centenas, 2 dezenas e 6 unidades
o	12 = 1 dezena e 2 unidades

Testar com: 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11,
1, 7 e 16

"""

lista = [326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11,
1, 7, 16]

for num in lista:
    centenas = num//100
    dezenas = (num%100)//10
    unidades = num%10

    saida = str(num) + ' = '

    if centenas > 0:
        saida += str(centenas) + ' centena'
        if centenas > 1:
            saida += 's'

        if dezenas > 0:
            if unidades > 0:
                saida += ', '
            else:
                saida += ' e '
        else:
            if unidades > 0:
                saida += ' e '

    if dezenas > 0:
        saida += str(dezenas) + ' dezena'
        if dezenas > 1:
            saida += 's'

        if unidades > 0:
            saida += ' e '

    if unidades > 0:
        saida += str(unidades) + ' unidade'
        if unidades > 1:
            saida += 's'

    print(saida)
