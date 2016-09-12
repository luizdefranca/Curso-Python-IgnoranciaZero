"""
Lista de comida
"""

def lista():
    start = 0
    lista = []
    def incrementa(item):
        nonlocal lista, start
        lista.append(item)
        start += 1
        print(item, start)
    return incrementa

compras1 = lista()

compras1('presunto')
compras1('mortadela')
compras1('queijo')
compras1('pão')
