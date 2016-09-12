"""
Escreva um Programa que imprime dois numeros de sua escolha
e que depois imprime a soma, a subtração, a multiplicação,
a divisão normal e a divisão inteira do maior pelo menor,
e o resto(coloque na mensagem a palavra resto ao invez do símbolo %)
da divisão do maior pelo menor

EXEMPLO DE SAÍDA:
>>> 
x = 15 
y = 10
15 + 10 = 25
15 - 10 = 5
15 x 10 = 150
15 / 10 = 1.5
15 // 10 = 1
15 resto 10 = 5
>>> 
"""
x = 15
y = 10

print("x =", x, "\ny =", y)
print(x, "+", y, "=", x+y)
print(x, "-", y, "=", x-y)
print(x, "x", y, "=", x*y)
print(x, "/", y, "=", x/y)
print(x, "//", y, "=", x//y)
print(x, "resto", y, "=", x%y)
