def main ():
    n = int(input("Digite n: "))
    x = float(input("Digite as coordenadas x do ponto 1: "))
    y = float(input("Digite as coordenadas y do ponto 1: "))
    ponto_m = [x,y]
    for i in range (1,n):
        x = float(input("Digite as coordenadas x do ponto %d: "%(i+1)))
        y = float(input("Digite as coordenadas y do ponto %d: "%(i+1)))
        ponto = [x,y]
        if angulo(ponto[0],ponto[1]) < angulo(ponto_m[0],ponto_m[1]):
            ponto_m = ponto
    print (ponto_m)
    
def modulo (y):
    if y < 0:
        y = -y
    return y

def arctan (x):
    k, arctan, n = 1, 0, 0
    while modulo(((x**(k))/k)*((-1)**(n))) >= 0.001:
        arctan += ((x**(k))/k)*((-1)**(n))
        k += 2
        n += 1
    return arctan

def angulo (x,y):
    if y>x:
        angulo = (3.14/2) - arctan(x/y)
    else:
        angulo = arctan(y/x)
    angulo *=(180/3.14)
    return angulo

main ()
