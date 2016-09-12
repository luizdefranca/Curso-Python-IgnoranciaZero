"""
Organize os elementos de uma lista em ordem crescente
"""

a = [5,3,1,2,4]
aux = a[:]
b = []
print("lista = ",a)
"""
while len(b) != len(a):
    menor = aux[0]
    for ele in aux:
        if ele < menor:
            menor = ele

    b.append(menor)
    aux.remove(menor)

a = b
"""

a.sort()

print("lista = ",a)
    
