"""
Método get

Escreva uma função que recebe um dicionário, uma chave, e opcionalmente
um valor, e se a chave estiver no dicionário devolve o valor contido
nessa chave, caso contrário devolve o valor passado para a funçao
"""
contato = {'Nome' : 'Pedro', 'Telefone': 12345678, 'Email': 'pedro.henrique.forli@usp.br',
            'Endereço': 'Av. Paulista'}

def get(dic, key, valor = None):
    if key in dic:
        return dic[key]
    else:
        return valor

print(get(contato, 'Nome'))
print(get(contato, 'Celular', 88888888))
