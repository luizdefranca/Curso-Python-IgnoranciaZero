"""
Dados x real e n natural, calcular uma aproximação para cos x através dos
n primeiros termos da seguinte série:
cos x = 1/1 - (x**2)/2! + (x**4)/4! - (x**6)/6! + ... + ((-1)**k)*(x**2k)/((2k)!)

Compare com os resultados de sua calculadora!
"""
#2 termo = 1 termo * -x**2/2*1 --> i = 1 /  2*i = 2 / 2*i - 1 = 1
#3 termo = 2 termo * -x**2/4*3 --> i = 2 / 2*i = 4 / 2*1 - 1 = 3
#4 termo = 3 termo * -x**2/6*5
n = int(input("Digite n: "))
x = float(input("Digite x: "))

cos = termo = 1

for i in range(1, n+1):
    termo *= (-(x**2)/(2*i*(2*i-1)))
    cos += termo

print("O cosseno de", x, "é", cos)



