#Adição de Termos da direita para a esquerda
soma = 0.0
for n in range (10000, 0, -1):
    x = ((-1)**(n-1))*(1/n)
    soma += x
print (soma)

#Adição de termos da esquerda para a direita
soma = 0.0
for n in range (10000):
    x = ((-1)**n)*(1/(n+1))
    soma += x
print (soma)

#Adição separada dos termos positivos dos termos negativos da esquerda para a direita
soma_p = soma_n = 0.0
for n in range (10000):
    x = ((-1)**n)*(1/(n+1))
    if x > 0:
        soma_p += x
    else:
        soma_n += x
soma = soma_p + soma_n
print (soma_p, soma_n, soma)

#Adição separada de termos positivos dos termos negativos da direita para a esquerda

soma_p = soma_n = 0.0
for n in range (10000, 0, -1):
    x = ((-1)**(n-1))*(1/n)
    if x > 0:
        soma_p += x
    else:
        soma_n += x
soma = soma_p + soma_n
print (soma_p, soma_n, soma)
