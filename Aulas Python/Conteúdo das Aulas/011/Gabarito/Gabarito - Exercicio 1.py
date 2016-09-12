"""
Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
	Observando os termos no plural a colocação do "e", da vírgula
	entre outros. Exemplo:
	326 = 3 centenas, 2 dezenas e 6 unidades
	12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
	101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

num = int(input("Digite o numero: "))
aux = num
if num < 1000:
    centenas = aux //100
    aux = aux %100

    dezenas = aux //10
    aux = aux % 10

    unidades = aux // 1

    if num >= 100:
        if centenas > 1:
            if dezenas > 1:
                if unidades > 1:
                    print(num, "=",centenas, "centenas,", dezenas, "dezenas e", unidades, "unidades")
                else:
                    print(num, "=",centenas, "centenas,", dezenas, "dezenas e", unidades, "unidade")
            else:
                if unidades > 1:
                    print(num, "=",centenas, "centenas,", dezenas, "dezena e", unidades, "unidades")
                else:
                    print(num, "=",centenas, "centenas,", dezenas, "dezena e", unidades, "unidade")
        else:
            if dezenas > 1:
                if unidades > 1:
                    print(num, "=",centenas, "centena,", dezenas, "dezenas e", unidades, "unidades")
                else:
                    print(num, "=",centenas, "centena,", dezenas, "dezenas e", unidades, "unidade")
            else:
                if unidades > 1:
                    print(num, "=",centenas, "centena,", dezenas,"dezena e", unidades, "unidades")
                else:
                    print(num, "=",centenas, "centena,", dezenas,"dezena e", unidades, "unidade")
            
    elif 10 <= num < 100:
        if dezenas > 1:
            if unidades > 1:
                print(num, "=",dezenas, "dezenas e", unidades, "unidades")
            else:
                print(num, "=",dezenas, "dezenas e", unidades, "unidade")
        else:
            if unidades > 1:
                print(num, "=",dezenas, "dezena e", unidades, "unidades")
            else:
                print(num, "=",dezenas, "dezena e", unidades, "unidade")
    else:
        if unidades > 1:
            print(num, "=",unidades, "unidades")
        else:
            print(num, "=",unidades, "unidade")
else:
    print("O numero é maior ou igual a mil, o programa nao pode ser executado")

