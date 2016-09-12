m = int(input("Digite m: "))
n = 1
for n in range(m+1):
    soma, cont, x, aux = 0, 1, 1, n
    for cont in range(n):
        soma = soma + 2*cont

    while x <= aux**3:
        if aux**3 == x*aux + soma:
            print ("O número", aux, "elevado ao cubo tem como soma: ")
            while aux - 1 >= 0:
                r = x + 2*(aux - 1)
                print (r)
                aux -= 1
            x = aux**3
        x += 1
