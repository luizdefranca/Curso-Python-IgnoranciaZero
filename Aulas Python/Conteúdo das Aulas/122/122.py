print("1 - getattr, setattr")

class Vazio:
    def __getattr__(self, atr_nome):
        if atr_nome == 'idade':
            return 40
        else:
            raise AttributeError(atr_nome)

e = Vazio()
print(e.idade)

try:
    e.nome
except AttributeError as E:
    print(E)


class ControleAcesso:
    def __setattr__(self, atr, valor):
        if atr == 'idade':
            self.__dict__[atr] = valor + 10
        else:
            raise AttributeError(atr + ' não permitido')


c = ControleAcesso()
c.idade = 40
print(c.idade)


try:
    c.nome = "Lucas"
except AttributeError as E:
    print(E)

input()

print("Utilidade: Controle no acesso de atributos não definidos")
print("OBS: getattribute --> para atributos que existem")
input()

#######################################

print("2 - setitem, getitem --> Para dicionários")

class Vazio:
    def __getitem__(self, atr_nome):
        if atr_nome == 'idade':
            return 40
        else:
            raise AttributeError(atr_nome)

e = Vazio()
print(e['idade'])

try:
    e['nome']
except AttributeError as E:
    print(E)

class ControleAcesso:
    def __setitem__(self, atr, valor):
        if atr == 'idade':
            self.__dict__[atr] = valor + 10
        else:
            raise AttributeError(atr + ' não permitido')


c = ControleAcesso()
c['idade'] = 40
print(c.idade)

try:
    c['nome'] = "Lucas"
except AttributeError as E:
    print(E)

input()

print("Utilidade: Criação dos próprios dicionários")
input()

##############################

print('3 - Objetos Chamáveis --> Funções')

class Op_Basicas:
    def __call__(self, qualquer_coisa):
        return qualquer_coisa

o = Op_Basicas()

print(o("Sou uma instância chamável"))

input()

print("Utilidade principal: Tkinter")
print("Podemos definir como command para uma dada widget do")
print("tkinter como sendo um objeto chamável, assim poderíamos")
print("com facilidade manipular os atributos do objeto além de")
print("utilizar outros métodos de forma a obter mair controle sobre")
print("o aplicativo")

input()

