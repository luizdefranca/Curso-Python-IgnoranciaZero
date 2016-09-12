"""
Construa o seu próprio objeto
range
"""
#Lembre-se podemos ter mais de um range ao mesmo
#tempo, logo podemos ter:

class meu_range(object):
    def __init__(self, *especificações):
        if len(especificações) == 0:
            raise TypeError("range expected 1 arguments, got 0")
        elif len(especificações) == 1:
            self.com = 0
            self.fim = especificações[0]
            self.inc = 1
        elif len(especificações) == 2:
            self.com = especificações[0]
            self.fim = especificações[1]
            self.inc = 1
        elif len(especificações) == 3:
            self.com = especificações[0]
            self.fim = especificações[1]
            self.inc = especificações[2]
        
        try:
            assert type(self.com) == int
            assert type(self.fim) == int
            assert type(self.inc) == int
        except AssertionError:
            raise TypeError("object cannot be interpreted as an integer")
        
        try:
            assert self.inc != 0
        except AssertionError:
            raise ValueError("range() arg 3 must not be zero")
    
    def __iter__(self):
        return range_iter(self.com, self.fim, self.inc)
    
    def __str__(self):
        if self.inc == 1:
            return "range(%i, %i)"%(self.com, self.fim)
        else:
            return "range(%i, %i, %i)"%(self.com, self.fim, self.inc)
    
class range_iter(object):
    def __init__(self, com, fim, inc):
        self.com = com
        self.inc = inc
        self.fim = fim
    def __next__(self):
        if (self.com < self.fim and self.inc > 0) or (self.com > self.fim and self.inc < 0):
            retorno = self.com
            self.com += self.inc
            return retorno
        else:
            raise StopIteration

#TESTES
testes = [(5,), (1.7,), ("opa",), (), (1,5,0), (1,5), (5,2), (5,2,-1)]

for t in testes:
    print("Teste: FOR I IN RANGE%s"%str(t))
    
    try:
        print("Resultados da iteração:", end = " ")
        for i in meu_range(*t):
            print(i, end = " ")

        print("\nObjeto range: %s"%meu_range(*t))

        print("Iterador: %s"%iter(meu_range(*t)))
    
    except (TypeError, ValueError) as e:
        print(e)

    print()

#Ou
"""
class meu_range(object):
    def __init__(self, *especificações):
        if len(especificações) == 0:
            raise TypeError("range expected 1 arguments, got 0")
        elif len(especificações) == 1:
            self.com = 0
            self.fim = especificações[0]
            self.inc = 1
        elif len(especificações) == 2:
            self.com = especificações[0]
            self.fim = especificações[1]
            self.inc = 1
        elif len(especificações) == 3:
            self.com = especificações[0]
            self.fim = especificações[1]
            self.inc = especificações[2]
       
        try:
            assert type(self.com) == int
            assert type(self.fim) == int
            assert type(self.inc) == int
        except AssertionError:
            raise TypeError("object cannot be interpreted as an integer")
        
        try:
            assert self.inc != 0
        except AssertionError:
            raise ValueError("range() arg 3 must not be zero")
    
    def __iter__(self):
        class range_iter(object):
            def __init__(self, com, fim, inc):
                self.com = com
                self.inc = inc
                self.fim = fim
            def __next__(self):
                if self.com <= self.fim:
                    retorno = self.com
                    self.com += self.inc
                    return retorno
                else:
                    raise StopIteration

        return range_iter(self.com, self.fim, self.inc)

    def __str__(self):
        if self.inc == 1:
            return "range(%i, %i)"%(self.com, self.fim)
        else:
            return "range(%i, %i, %i)"%(self.com, self.fim, self.inc)   
"""
