print("Propriedades e Descritores")
input()

print("Propriedades - Permitem gerenciar a criação")
print("e manipulação de atributos de uma da classe")
print("Semelhante aos métodos __getattr__, __setattr")
print("e __getattribute__ porem menos genéricos")
input()

print("Exemplo")

class Pessoa(object):
    def __init__(self, nome):
        self._nome = nome
    def getNome(self):
        print('Obtendo...')
        return self._nome
    def setNome(self, valor):
        print('Modificando...')
        self._nome = valor
    def delNome(self):
        print('Removendo...')
        del self._name
    nome = property(getNome, setNome, delNome, "Documentação da propriedade nome")

bob = Pessoa('Bob Smith')
print(bob.nome)
bob.nome = 'Robert Smith'
print(bob.nome)
print('-'*20)
sue = Pessoa('Sue Jones')
print(sue.nome)
print(Pessoa.nome.__doc__)

input()

print("Descritores - Funcionam como propriedades")
print("entretanto os métodos get, set, del e a descrição")
print("são todos feitos por uma classe específica com")
print("protocolo bem definido")
input()

class Nome(object):
    "Documentação da propriedade nome"
    def __get__(self, instancia, dono):
        print('Obtendo...')
        return instancia._nome
    def __set__(self, instancia, valor):
        print('Modificando...')
        instancia._nome = valor
    def __delete__(self, instancia):
        print('Removendo...')
        del instancia._nome

class Pessoa(object):
    def __init__(self, nome):
        self._nome = nome
    nome = Nome()

nome = Nome()
bob = Pessoa('Bob Smith')
print(bob.nome)
bob.nome = 'Robert Smith'
print(bob.nome)
del bob.nome
print('-'*20)
sue = Pessoa('Sue Jones')
print(sue.nome)
print(Nome.__doc__)
input()

print("A função 'property' em python é usada para criar")
print("um descritor")
input()
