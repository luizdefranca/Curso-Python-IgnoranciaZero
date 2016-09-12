def main ():
    n = int(input("Digite n: "))
    for i in range (n):
        dia = int(input("Digite o dia: "))
        mes = int(input("Digite o mês: "))
        ano = int(input("Digite o ano: "))
        print (seguint(dia, mes, ano))
def bissexto(ano):
    resp = 0
    if ano %4 == 0:
        resp = 1
    return resp
def seguinte (dia, mes, ano):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 10 or mes == 11 or mes == 12:
        maximo = 31
    elif mes == 4 or mes == 6 or mes == 8 or mes == 9:
        maximo = 30
    elif mes == 2 and bissexto(ano) == 1:
        maximo = 29
    else:
        maximo = 28
    dia += 1
    if dia > maximo:
        mes += 1
        dia = 1
    if mes > 12:
        ano += 1
        mes = 1
    return dia, mes, ano
main ()
