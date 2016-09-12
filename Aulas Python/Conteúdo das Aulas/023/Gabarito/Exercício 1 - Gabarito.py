"""
Dados x e E reais,  > 0, calcular uma aproximação para sen x através da seguinte
série infinita

sen x = x/(1!) - (x**3)/(3!) + (x**5)/(5!) -...+((-1)**k)*(x**(2*k+1))/((2*k+1)!)
    
      incluindo todos os termos até que

modulo(x**(2*k+1))/((2*k+1)!) < E

     Compare com os resultados de sua calculadora! 
"""

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
