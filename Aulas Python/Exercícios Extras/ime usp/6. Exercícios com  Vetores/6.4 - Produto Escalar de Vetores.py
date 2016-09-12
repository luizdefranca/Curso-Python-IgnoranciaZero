def main ():
    n = int(input("Digite o número de elementos: "))
    x = cord (n)
    y = cord (n)
    soma = 0.0
    for i in range (n):
        soma += x[i]*y[i]
    print(soma)
def cord (n):
    lista = []
    for j in range (n):
        ele = float(input("Digite a coordenada %d de %d: "%(j+1, n)))
        lista.append(ele)
    return lista
main ()
