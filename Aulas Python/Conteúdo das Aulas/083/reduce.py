#Reduce
#--> Recebe um objeto iterável e combina
#    utiliza uma função para combinar
#    o resultado da função anterior com
#    o elemento seguinte do objeto iterável
import functools

def olhe_soma(x, y):
	print ('Adicionando', x, 'a', y)
	return x + y


print(functools.reduce(olhe_soma, [1, 2, 3, 4, 5]))

#Caiu em desuso pois um
#for loop é muito mais usado

#Algoritmo do reduce
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
