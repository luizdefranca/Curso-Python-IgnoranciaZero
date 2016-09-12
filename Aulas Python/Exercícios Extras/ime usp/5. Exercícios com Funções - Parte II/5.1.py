def main ():
    n = int(input("Digite n: "))
    for i in range (n):
        num = int(input("Digite o número %d de %d: "%(i+1,n)))
        cont, dig = n_digitos(num)
        print ("O número de dígitos é: %d / O primeiro digito é: %d"%(cont,dig))

def n_digitos(n):
    cont = 0
    while n!=0:
        dig = n%10
        n //=10
        cont += 1
    return cont, dig
main ()
