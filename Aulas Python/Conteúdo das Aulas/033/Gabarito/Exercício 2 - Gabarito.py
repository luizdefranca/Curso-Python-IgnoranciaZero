"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M.
como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as
conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores
de entrada todas as vezes que desejar.
"""

def ConverteHorário(hora):
    return hora - 12

def imprimeHora(hora, minuto):
    if hora <= 12:
        print("%i:%i A.M."%(hora, minuto))
    else:
        hora = ConverteHorário(hora)
        print("%i:%i P.M."%(hora, minuto))

rodando = True
while rodando:
    hora = int(input("Digite a hora: "))
    minuto = int(input("Digite os minutos: "))
    imprimeHora(hora, minuto)
    rodando = bool(int(input("Deseja fazer uma nova conversão(1 - sim/0 - não): ")))
    
