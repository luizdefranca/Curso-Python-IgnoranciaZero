"""
Dados três números naturais,
verificar se eles formam os lados de um triângulo retângulo. 
"""

a = int(input("Digite o primeiro: "))
b = int(input("Digite o segundo: "))
c = int(input("Digite o terceiro: "))
if c*c == b*b + a*a or b*b == a*a + c*c or a*a == b*b + c*c:
    print ("O triângulo", a, b, c, "é retângulo.")
else:
    print ("O triângulo", a, b, c, "não é retângulo.")
