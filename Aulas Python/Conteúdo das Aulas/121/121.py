import time

print("Para construir objetos indexáveis precisamos construir alguns")
print("alguns métodos mágicos específicos dentro do nosso objeto")
print("são eles: __getitem__, __setitem__, __len__, __delitem__")
input()

print("__getitem__ --> Permite pegar o objeto contido no indice")
print("pedido. Exemplo:")

class MinhaLista(object):
    def __getitem__(self, index):
        return index ** 2

a = MinhaLista()

for i in range(5):
    print(a[i])

input()

print("O que acontece se eu tentar percorrer esse objeto com um for loop?")

t0 = time.time()
for i in a:
    print(i)
    tf = time.time()
    if tf - t0 > 5:
        break

input()

print("Veja que a lista não tem um limite por isso o for loop")
print("é infinito. Poderíamos corrigir isso fazendo:")

class MinhaLista(object):
    def __init__(self, tamanho):
        self.len = tamanho
        
    def __getitem__(self, index):
        if index < self.len:
            return index ** 2
        else:
            raise StopIteration 

a = MinhaLista(5)

for i in a:
    print(i)

input()

print("ou")


class MinhaLista(object):
    def __init__(self, *args):
        self.data = []
        for arg in args:
            self.data.append(arg)
        
    def __getitem__(self, index):
        return self.data[index]**2

a = MinhaLista(0,1,2,3,4)

for i in a:
    print(i)

input()

print("É possível usar slices neles a partir desse método")
print("slice é um objeto em python")
print("por exemplo slice(1,5,2) = ", slice(1,5,2))
input()

print("Assim poderíamos obter o slice da seguinte forma: ")

class MinhaLista:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)
                

a = MinhaLista()

a[1]
a[1:3]

input()

print("Assim como podemos obter o valor de uma determinada posição")
print("para colocar um valor numa dada posição é preciso um método")
print("especial, no caso o método __setitem__")
input()

class SequenciaAritimetica:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.modificado = {}

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0: raise IndexError
            try: return self.modificado[index]
            except KeyError: return self.start + index*self.step
        else:
            if index.step == None: step = 1
            else: step = index.step
            data = []
            for i in range(index.start, index.stop, step):
                data.append(self[i])
            return data

    def __setitem__(self, index, value):
        if index < 0: raise IndexError
        self.modificado[index] = value

s = SequenciaAritimetica(2, 3)

print(s[3])
s[3] = 4
print(s[3])
print(s[1:5])

input()

print("Para deletar uma chave é preciso utilizar o método")
print("__delitem__")

class SequenciaAritimetica:
    def __init__(self, start=0, end=1, step=1):
        self.start = start
        self.step = step
        self.end = end
        self.data = list(range(start, end, step))

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0: raise IndexError
            try: return self.modificado[index]
            except KeyError: return self.data[index]
        else:
            return self.data[index]

    def __setitem__(self, index, value):
        if index < 0: raise IndexError
        self.data[index] = value
    
    def __delitem__(self, index):
        del self.data[index]

s = SequenciaAritimetica(1, 6)
del s[1]
print(s.data)

input()

print("Por fim para obter o tamanho de um objeto temos de colocar")
print("o método especial __len__")

class SequenciaAritimetica:
    def __init__(self, start=0, end=1, step=1):
        self.start = start
        self.step = step
        self.end = end
        self.data = list(range(start, end, step))
        self.len = len(self.data)

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0: raise IndexError
            try: return self.modificado[index]
            except KeyError: return self.data[index]
        else:
            return self.data[index]

    def __setitem__(self, index, value):
        if index < 0: raise IndexError
        self.data[index] = value
    def __delitem__(self, index):
        del self.data[index]
    def __len__(self):
        return self.len

s = SequenciaAritimetica(1, 6)
print(len(s))

input()

print("E se um elemento está contido dentro do objeto")
print("utilizando o método __contains__")

class SequenciaAritimetica:
    def __init__(self, start=0, end=1, step=1):
        self.start = start
        self.step = step
        self.end = end
        self.data = list(range(start, end, step))
        self.len = len(self.data)

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0: raise IndexError
            try: return self.modificado[index]
            except KeyError: return self.data[index]
        else:
            return self.data[index]

    def __setitem__(self, index, value):
        if index < 0: raise IndexError
        self.data[index] = value
    def __delitem__(self, index):
        del self.data[index]
    def __len__(self):
        return self.len
    def __contains__(self, value):
        return value in self.data

s = SequenciaAritimetica(1, 6)
print(2 in s)
print(2 not in s)

input()
