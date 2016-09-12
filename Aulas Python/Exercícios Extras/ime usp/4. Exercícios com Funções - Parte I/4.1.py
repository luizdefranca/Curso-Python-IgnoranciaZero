def main ():
    a = int(input("Digite a: "))
    b = int(input("Digite b: "))
    resp = True
    d = 0
    while resp and d<10:
        cont_a = contadigitos(a,d)
        cont_b = contadigitos(b,d)
        if cont_a != cont_b:
            resp = False
            print ("%d não é permutação de %d" %(a,b))
        d += 1
    if resp:
        print ("%d é permutação de %d" %(a,b))
def contadigitos (n,d):
    cont = 0
    while n!=0:
        dig = n%10
        if dig == d:
            cont+= 1
        n//=10
    return cont

main ()
