class Quadrados(object):
    def __init__(self, com, fim):
	self.com = com
	self.fim = fim
    def __iter__(self):
	return self
    def __next__(self):
	if self.com < self.fim:
	    self.com += 1
	    return self.com**2
	else:
	    raise StopIteration

#1 - Criar cópias
x = Quadrados(0,5)
y = Quadrados(0,5)

#2 - Conversão para lista
l = list(Quadrados(0,5))

#3 - Classe iteradora != iteravel
class Quadrados3(object):
    def __init__(self, com, fim):
	self.com = com
	self.fim = fim
    def __iter__(self):
	return Quadrados_Iter(self, self.com, self.fim)

class Quadrados_Iter(object):
    def __init__(self, com, fim):
	self.com = com
	self.fim = fim
    def __next__(self):
	if self.com < self.fim:
	    self.com += 1
	    return self.com**2
	else:
	    raise StopIteration

#4 - Geradores
class Quadrados2(object):
    def __init__(self, com, fim):
	self.com = com
	self.fim = fim
    def __iter__(self):
	for i in range(self.com + 1, self.fim + 1):
	    yield i**2
