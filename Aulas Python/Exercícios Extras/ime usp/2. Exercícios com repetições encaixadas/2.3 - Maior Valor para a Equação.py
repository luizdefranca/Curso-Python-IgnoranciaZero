"""
Dados dois naturais m e n determinar, entre todos os pares de números naturais
(x,y) tais que x < m e y < n, um par para o qual o valor da expressão
x*y - x**2 + y seja máximo e calcular também esse máximo.
"""


n = int(input("Digite n: "))
m = int(input("Digite m: "))
Xmax = Ymax = Vmax = 0

x = y = 0
for x in range(m):
    for y in range(n):
        if x*y - x*x + y > Vmax:
            Vmax = x*y - x*x + y
            Xmax = x
            Ymax = y

print ("O maior par é (%i,%i) e seu valor máximo é %i" %(Xmax, Ymax, Vmax))
