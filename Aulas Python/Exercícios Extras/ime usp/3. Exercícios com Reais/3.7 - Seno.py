x = float(input("Digite o ângulo em radianos: "))
e = float(input("Digite e: "))
k, termo, sen = 1, x, x
teste = True
while teste:
    termo *= (-1)*((x**2)/((2*k + 1)*(2*k)))
    teste2 = termo
    if teste2 < 0:
        teste2 *= (-1)
    if teste2 >= e:
        sen += termo
    else:
        teste = False
print ("O seno de %.3g é %.10g" %(x, sen))
from math import sin
print("O seno de %.3g, na calculadora, é %.10g"%(x, sin(x)))
