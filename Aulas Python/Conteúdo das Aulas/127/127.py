print("Vamos estudar agora decoradores de métodos")
print("e decoradores de classes.")

input()

print("Decoradores de métodos funcionam assim como")
print("decoradores de classe, dessa forma basta criar")
print("uma função decoradora e aplica-la a um método")
print("usando a sintaxe do @")

input()

print("Alguns decoradores de método populares apresentaremos")
print("agora. São eles @staticmethod, @classmethod, @override e @property")

input()

print("@staticmethod indica que o dado método é estatico")
print("logo deverá ser chamado usando a classe e não uma")
print("instância da classe, assim a instância não")
print("deve ser passada como argumento. Por exemplo: ")

class A(object):
    @staticmethod
    def method(*argv):
        return argv

a = A()

print("a.method([1,2,3,4]) = ", a.method([1,2,3,4]))
print("Sem o @staticmethod")

class A(object):
    def method(*argv):
        return argv

a = A()
print("a.method([1,2,3,4]) = ", a.method([1,2,3,4]))

input()

print("@classmethod, ao inves da instância ser passada")
print("como argumento para o método, a classe será passada")

class A(object):
     @classmethod
     def method(*argv):
         return argv

a = A()

print("a.method([1,2,3,4]) =", a.method([1,2,3,4]))

input()

print("@override não é um decorador pré construido em python")
print("entretanto é um 'decorador' bastante popular em outras")
print("em outras linguagens, especialmente Java. Podemos escrever")
print("uma receita de bolo simples para esse decorador como sendo:")

input()

def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider

input()

print("A única coisa que o @override faz é previnir")
print("erros de digitação ao criar um método de uma classe")
print("filha que irá sobrepor o método da classe pai.")

input()

class Pai(object):
    def meu_metodo(self):
        print('Ola Mundo!')


class Filha(Pai):
    @overrides(Pai)
    def meu_metodo(self):
        print('Ola Marte!')

try:
    class Erro(Pai):
        @overrides(Pai)
        def mei_metodo(self):
            print('ops!')
except AssertionError:
    print("Pegamos erro")
    
input()

print("Um decorador importante refere-se as propriedades")
print("Veja no exemplo que por meio dos decoradores substituimos")
print("A linha de criação da propriedade e ainda todos os métodos")
print("possuem os mesmos nomes")

class Pessoa:
    def __init__(self, prim_nome, ult_nome):
        self.prim_nome = prim_nome
        self.ult_nome = ult_nome

    @property
    def nome(self):
        return '%s, %s' % (self.ult_nome, self.prim_nome)

    @nome.setter
    def nome(self, valor):
        self.prim_nome = valor

    @nome.deleter
    def nome(self):
        del self.prim_nome
        del self.ult_nome

p = Pessoa('Luis', 'Rodrigo')
print(p.nome)
p.nome = 'Alchin, Martin'
print(p.nome)
del p.nome

input()

print("Podemos criar decoradores de classes, isto é")
print("decoradores que irão mudar todo o funcionamento")
print("de uma dada classe")

input()

print("No exemplo abaixo vemos o decorador 'singleton' que")
print("faz com que apenas uma instância de classe possa ser")
print("criada")

instancias = {}
def singleton(umaClasse):
    def onCall(*args, **kwargs):
        print("onCall foi chamado agora!!")
        if umaClasse not in instancias:
            instancias[umaClasse] = umaClasse(*args, **kwargs)
        return instancias[umaClasse]
    return onCall

@singleton
class Pessoa:
    def __init__(self, nome, horas, ganho):
        self.nome = nome
        self.horas = horas
        self.ganho = ganho
    def paga(self):
        return self.horas * self.ganho

bob = Pessoa('Bob', 40, 10)
print(bob.nome, bob.paga())
sue = Pessoa('Sue', 50, 20)
print(sue.nome, sue.paga())


input()

print("Uma classe decoradora por outro lado")
print("consiste numa classe que irá decorar a outra")
print("logo a classe decoradora deverá receber uma")
print("classe como argumento")

input()

print("Por exemplo, suponhamos que se queira acompanhar os métodos")
print("usados por uma determinada classe. Iremos criar uma classe")
print("decoradora Trace que permitira acompanhar a execução de")
print("uma classe decorada por ela")

input()

class Tracer:
    def __init__(self, umaClasse):
        print("Construtor foi chamado!!")
        self.umaClasse = umaClasse
    def __call__(self, *args):
        print("Chamamos o método __call__")
        self.wrapped = self.umaClasse(*args)
        return self
    def __getattr__(self, atrnome):
        print('Trace: ' + atrnome)
        return getattr(self.wrapped, atrnome)

@Tracer # Chama o construtor de Tracer
class Spam:
    def display(self):
        print('Spam!' * 8)

print("Vamos começar o teste...")
s = Spam() # Chama o Call de Tracer
s.display()

input()
