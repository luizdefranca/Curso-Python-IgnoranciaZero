"""
Dados três números naturais,
verificar se eles formam os lados de um triângulo retângulo.

lado1**2 + lado2**2 == lado3**2
lado3**2 + lado1**2 == lado2**2
lado2**2 + lado3**2 == lado1**2
"""
lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))


if lado1**2 + lado2**2 == lado3**2 or lado3**2 + lado1**2 == lado2**2 or lado2**2 + lado3**2 == lado1**2:
    print("O triângulo é retângulo.")
else:
    print("O triângulo não é retângulo.")
