print("Formatação na base de dicionários")
print("semelhante a formatação do normal de strings")
print("'Mais %(qtd)d %(comida)s' % {'qtd': 1, 'comida': 'presunto'}")
print('Mais %(qtd)d %(comida)s' % {'qtd': 1, 'comida': 'presunto'})
print("Note que temos o nome do que estamos substituindo assim")
print("como o tipo que estaremos colocando")

input()

print("Templates por outro lado constituem numa")
print("substituição um pouco distinta")
print("por exemplo template = '{0}, {1} e {2}'")
print("indica a construção de um template.")
template = '{0}, {1} e {2}'

input()

print("A diferença de um template é que a substituição")
print("pode ser feita diversas vezes por meio do método format")
print("Então se fizessemos: template.format('queijo', 'presunto', 'ovos')")
print("receberiamos de volta as seguintes strings:")
print(template.format('queijo', 'presunto', 'ovos'))

input()

print("Além disso podemos construir templates por palavras")
print("chaves: template = '{numero}, {porco} e {comida}'")
template = '{numero}, {porco} e {comida}'
print("template.format(numero=1, porco='presunto', comida='ovos')")
print(template.format(numero=1, porco='presunto', comida='ovos'))

input()

print("Podemos usar até mesmo os dois")
print("""
template = '{numero}, {0} e {comida}'
template.format('presunto', numero=1, comida='ovos')
"""
      )
template = '{numero}, {0} e {comida}'
print(template.format('presunto', numero=1, comida='ovos'))

input()

import sys
print("Podemos usar modificações especiais na hora de formar")
print("templates, por exemplo: ")
print("'Meu {1[tipo]} roda {0.platform}'.format(sys, {'tipo': 'laptop'})")
print('Meu {1[tipo]} roda {0.platform}'.format(sys, {'tipo': 'laptop'}))
lista = list("ABACATE")
print("'primeiro={0[0]}, terceiro={0[2]}'.format(lista)")
print('primeiro={0[0]}, terceiro={0[2]}'.format(lista))

input()

print("Podemos especificar também o número de caracteres")
print("que uma determinada expressão poderá ocupar")
print("""'{0:10} = {1:10}'.format('spam', 123.4567)
'{0:>10} = {1:<10}'.format('spam', 123.4567)
'{0.platform:>10} = {1[tipo]:<10}'.format(sys, dict(tipo='laptop'))""")
print('{0:10} = {1:10}'.format('spam', 123.4567), '{0:>10} = {1:<10}'.format('spam', 123.4567),
      '{0.platform:>10} = {1[tipo]:<10}'.format(sys, dict(tipo='laptop')), sep = "\n")

input()

print("Podemos até especificar algumas formatações numéricas: ")
print("'{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159)")
print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
print("'{0:X}, {1:o}, {2:b}'.format(255, 255, 255)")
print('{0:X}, {1:o}, {2:b}'.format(255, 255, 255))
print("'{0:.{1}f}'.format(1 / 3.0, 4)")
print('{0:.{1}f}'.format(1 / 3.0, 4))

input()

print("Python também possuí uma classe específica")
print("para lidar com templates que está contida no")
print("módulo string")
import string
t = string.Template('$num = $title')
print(t.substitute({'num': 7, 'title': 'Strings'}))
print(t.substitute(num=7, title='Strings'))
print(t.substitute(dict(num=7, title='Strings')))

input()
