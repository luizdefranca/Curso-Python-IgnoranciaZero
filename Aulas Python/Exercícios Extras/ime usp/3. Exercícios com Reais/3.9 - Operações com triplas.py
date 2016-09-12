n = int(input("Digite n: "))
for i in range (n):
    op = input("Digite o operador %d de %d: "%(i+1, n))
    a = float(input("Digite o primeiro número da tripla %d de %d: "%(i+1, n)))
    b = float(input("Digite o segundo número da tripla %d de %d: "%(i+1, n)))
    tripla = []
    tripla.append(op)
    tripla.append(a)
    tripla.append(b)
    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a*b
    else:
        res = a/b
    print ("A tripla", tripla, "tem resultado", res)
              
