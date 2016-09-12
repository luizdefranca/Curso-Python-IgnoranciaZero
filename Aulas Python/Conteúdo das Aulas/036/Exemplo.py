
def incrementa():
    global X
    incremento = 5 #variável local
    X += incremento #cópia do valor de x

X = 10

incrementa()


print(X)

