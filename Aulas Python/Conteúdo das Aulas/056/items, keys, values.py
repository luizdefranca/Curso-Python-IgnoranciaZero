"""
Métodos items, keys, values

Escreva três funções(todas recebendo um dicionário):
items: Uma imprime umas lista de tuplas, sendo que cada tupla contem a chave e o
valor da chave para o dicionário

keys: Uma que imprime uma lista contendo todas as chaves do dicionário

values: Uma que imprime uma lista contendo todos os valores de chave
do dicionário
"""
contato = {'Nome' : 'Pedro', 'Telefone': 12345678, 'Email': 'pedro.henrique.forli@usp.br',
            'Endereço': 'Av. Paulista'}
def items(dic):
    lista = []
    for key in dic:
        lista.append((key, dic[key]))

    print(lista)

def keys(dic):
    lista = []
    for key in dic:
        lista.append(key)

    print(lista)

def values(dic):
    lista = []
    for key in dic:
        lista.append(dic[key])

    print(lista)

items(contato)
keys(contato)
values(contato)
