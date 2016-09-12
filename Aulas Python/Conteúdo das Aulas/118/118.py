print("""Dicionários são extremamente úteis, mas às vezes você pode
ter um conjunto fixo de chaves possíveis disponíveis, então
você não precisa de muita flexibilidade. Em vez disso,
Python usa namedtuples, que fornecem algumas das
mesmas funcionalidades, mas são muito mais eficiente porque
as instâncias não precisam de conter qualquer uma das
chaves, apenas os valores que lhes estão associados""")
input()

print("Para criar namedtuples primeiro é preciso importar o módulo collections")
from collections import namedtuple
input()

print("Podemos criar namedtuples da seguinte maneira:")
print("Ponto = namedtuple('Point', 'x y')")
print("ou Ponto = namedtuple('Point', 'x, y')")
print("ou Ponto = namedtuple('Point', ['x', 'y'])")
Ponto = namedtuple('Point', 'x y')
print("1 Argumento = Nome da namedtuple")
print("2 Argumento = Chaves separada por espaço")
input()

print("Podemos criar uma instância de ponto:")
print('ponto = Ponto(13, 15)')
ponto = Ponto(13, 15)
input()

print("Podemos obter os valores contidos nas chaves da seguinte forma:")
print("ponto")
print(ponto)
print("ponto.x, ponto.y")
print(ponto.x, ponto.y)
print("ponto[0], ponto[1]")
print(ponto[0], ponto[1])
input()

print("Um cuidado que se deve ter é com os nomes das chaves")
print("elas não podem ser começadas com _ ,um digito e não pode ser uma palavra reservada")
print("Pode-se setar o argumento rename=True e se houver alguma palavra")
print("inadequada ela será automaticamente renomeada")
input()

