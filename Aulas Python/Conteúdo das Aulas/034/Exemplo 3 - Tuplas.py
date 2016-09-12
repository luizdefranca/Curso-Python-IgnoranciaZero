#3 - Função que retorna várias coisas
"""
Escreva uma função que recebe dois números e devolve a soma e
a multiplicação entre os dois
"""

def opMat(num1, num2):
    soma = num1+num2
    return soma, num1*num2, num1/num2, num1-num2

a,b,c,d = opMat(2,3)

print(a, b,c,d)
