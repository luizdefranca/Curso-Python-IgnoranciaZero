def main ():
    n = int(input("Digite n: "))
    c = f()
    raios = []
    for i in range (n):
        p = f()
        raio = ((p[0] - c[0])**2 + (p[1] - c[1])**2)**(1/2)
        if raio not in raios:
            raios.append (raio)
    print (raios)
def f():
    lista = []
    for n in range (2):
        cord = float(input("Digite uma coordenada: "))
        lista.append(cord)
    return lista
main ()
