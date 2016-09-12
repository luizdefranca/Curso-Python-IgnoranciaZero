"""
Arquivo para .split() e .rsplit()

Escreva uma função que tem como separador padrão caracter
' ' e recebe uma string e devolve um lista contendo a string separada
de acordo com a ocorrência do separador

Exemplo
frase = "Ola meu nome é pedro"
split(frase)
['Ola', 'meu', 'nome', 'é', 'pedro']
"""
def split(frase, separador = ' '):
    lista = []
    palavra = ''
    i = 0

    while i < len(frase) + 1 - len(separador):
        if frase[i:i+len(separador)] != separador:
            palavra += frase[i]
        else:
            if palavra != '':
                lista.append(palavra)
            i += len(separador)
            palavra = ''
            continue

        i+= 1

    palavra += frase[i:]

    if palavra != '':
        lista.append(palavra)

    return lista

print(split('criptografar ou c ou decriptografar ou d', ' ou '))
