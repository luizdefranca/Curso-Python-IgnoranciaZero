"""
16.	Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer
as consistências, informando ao usuário nas seguintes situações:

    a.	Se o usuário informar o valor de A igual a zero, a equação não é do
    segundo grau e o programa não deve fazer pedir os demais valores,
    sendo encerrado;

    b.	Se o delta calculado for negativo, a equação não possui raizes reais.
    Informe ao usuário e encerre o programa;

    c.	Se o delta calculado for igual a zero a equação possui apenas uma raiz
    real; informe-a ao usuário;

    d.	Se o delta for positivo, a equação possui duas raiz reais; informe-as
    ao usuário;

"""

a = float(input("Digite o valor de a: "))
if a>0:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("Não há raízes reais")
    elif delta == 0:
        print("Há apenas uma raíz real igual a", -b/(2*a))
    else:
        print("Há duas raízes: ")
        print("Raíz 1:", (-b+delta**(1/2))/(2*a))
        print("Raíz 2:", (-b-delta**(1/2))/(2*a))

else:
    print("A equação não é do segundo grau")
