print("##### defaultdict #####")

print("""
Outro padrão comum usando dicionários é assumir sempre algum
valor padrão no caso de um chave não poder ser encontrada no mapeamento.
Este comportamento pode ser conseguida por meio da captura explicita da
KeyError levantada quando estiver acessando a chave ou usando o método get(),
que pode retornar a valor adequado, se a chave não foi encontrada.
Um exemplo deste modelo é usando um dicionário para rastrear quantas vezes cada
palavra aparece em algum texto.
    """)
input()

print("""
def conta_palavras(texto):
    contador = {}
    for palavra in texto.split(' '):
        corrente = contador.get(palavra, 0) # Faz com que sempre tenha um número
        contador[palavra] = corrente + 1
    return contador
    """)

def conta_palavras(texto):
    contador = {}
    for palavra in texto.split(' '):
        corrente = contador.get(palavra, 0) # Faz com que sempre tenha um número
        contador[palavra] = corrente + 1
    return contador

input()

print("conta_palavras('Bom Bom Bom é comer bombom')")
print(conta_palavras('Bom Bom Bom é comer bombom'))
input()

print("""
Em vez de ter que lidar com essa chamada get(), o módulo collections fornece uma classe defaultdict
que pode lidar com esse passo para você. Quando você cria-lo, você pode passar um objeto/função chamável como único argumento,
que será utilizado para criar um novo valor quando uma chave solicitada não existe. Na maioria dos casos, você pode simplesmente
fornecer um dos built-in, que irá fornecer um valor de base útil para trabalhar. No caso de
conta_palavras(), podemos usar int.
    """)
input()

print("""
from collections import defaultdict

def conta_palavras(texto):
    contador = defaultdict(int)
    for palavra in texto.split(' '):
        contador[palavra] += 1
    return contador
    """)

from collections import defaultdict

def conta_palavras(texto):
    contador = defaultdict(int)
    for palavra in texto.split(' '):
        contador[palavra] += 1
    return contador
input()

print("conta_palavras('Bom Bom Bom é comer bombom')")
print(conta_palavras('Bom Bom Bom é comer bombom'))
input()

print("##### deques #####")

from collections import deque

print("A razão para a utilidade do deque é que ele permite a anexação e pop eficientemente")
print("no início (para a esquerda), em oposição às listas. Como efeito colateral agradável, você também pode girar a")
print("elementos ( ou seja, transferi-los para a direita ou para a esquerda , envolvendo em torno das extremidades ) de forma eficiente.") 
print("deque objetos também têm estender e métodos extendleft , com estender a trabalhar como correspondente")
print("método de lista , e extendleft trabalhando de forma análoga ao appendleft . Note-se que os elementos do")
print("iteráveis ​​utilizado em extendleft aparece no deque em ordem inversa .")
input()

print("d = deque('ghi')")
d = deque('ghi')
print("for elem in d: print(elem.upper())")
for elem in d: print(elem.upper())
input()

print("d.append('j')")
d.append('j')
print(d)
print("d.appendleft('j')")
d.appendleft('j')
print(d)
input()

print("d.pop()")
print(d.pop())
print(d)
print("d.popleft()")
print(d.popleft())
print(d)
input()

print("list(d)")
print(list(d))
print("d[0], d[-1]")
print(d[0], d[-1])
print("len(d)")
print(len(d))
print("'h' in d")
print('h' in d)
print("d.reverse()")
d.reverse()
print(d)
print("d.count('i')")
print(d.count('i'))
print("d.remove('i')")
d.remove('i')
print(d)
input()

print("d.extend('jkl')")
d.extend('jkl')
print(d)
print("d.extendleft('efg')")
d.extendleft('efg')
print(d)
input()

print("d.rotate(1)")
d.rotate(1)
print(d)
print("d.rotate(-1)")
d.rotate(-1)
print(d)
input()

print("d.maxlen")
print(d.maxlen)
print("d = deque(d, maxlen = 5)")
d = deque(d, maxlen = 5)
print(d)
print("d.append('a')")
d.append('a')
print(d)
input()

print("d.clear()")
d.clear()
print(d)
input()
