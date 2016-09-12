def main ():
    a = int(input("Digite a: "))
    b = int(input("Digite b: "))
    resp = encaixa(a,b)
    if a>b:
        aux1 = a
        while not resp and aux1!=0:
            resp = encaixa(aux1,b)
            aux1//= 10
        if resp:
            print("%d é segmento de %d"%(b,a))
    else:
        aux2 = b
        while not resp and aux2!=0:
            resp = encaixa(aux2,a)
            aux2//= 10
        if resp:
            print("%d é segmento de %d"%(a,b))
    if not resp:
        print("Um não é segmento do outro")

def encaixa (a,b):
    resp = True
    while a != 0 and b!=0 and resp:
        dig_a = a%10
        dig_b = b%10
        if dig_a != dig_b:
            resp = False
        a//=10
        b//=10
    return resp
main ()
