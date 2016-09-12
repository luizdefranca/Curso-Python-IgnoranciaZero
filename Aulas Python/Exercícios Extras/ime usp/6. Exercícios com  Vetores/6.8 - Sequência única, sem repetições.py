def main ():
    m = int(input("Digite m: "))
    n = int(input("Digite n: "))
    lista_m = f(m)
    lista_n = f(n)
    lista2 = []
    f2 (lista_n, lista2)
    f2 (lista_n, lista2)
    print (lista2)
def f (i):
    lista = []
    for j in range (i):
        q = float(input("Digite o elemento %d de %d: "%(j+1, i)))
        lista.append(q)
    return lista
def f2 (lista1, lista2):
    for j in range (len(lista1)):
        if lista1[j] not in lista2:
            lista2.append(lista1[j])
    return lista2
main ()
