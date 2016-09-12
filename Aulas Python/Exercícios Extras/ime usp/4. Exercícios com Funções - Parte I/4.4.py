def main ():
    soma, cont , d = 0, 0, 1
    n = int(input("Digite n: "))
    while cont < n:
        if primo(d):
            soma += d
            cont +=1
        d +=1
    print (soma)

def primo (m):
    i = 2
    resp = True
    while resp and i < m:
        if m % i == 0:
            resp = False
        i+= 1
    return resp
main ()
