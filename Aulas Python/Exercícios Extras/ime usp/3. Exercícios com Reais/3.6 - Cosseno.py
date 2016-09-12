#Detalhe: Angulos tem de ser escritos em radianos
x = float(input("Digite o ângulo em radianos: "))
n = int(input("Digite n: "))
cos, termo = 1.0, 1.0
for i in range (1, n+1):
    termo *= ((x**2)/(2*i*(2*i - 1)))*(-1)
    cos += termo
print ("O cosseno de %.3f é %.3f"%(x, cos)) 
