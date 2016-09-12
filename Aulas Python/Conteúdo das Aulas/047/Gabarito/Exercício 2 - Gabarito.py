"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar
M-matutino ou V-Vespertino ou N- Noturno.

Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso.
"""
print("M - Matutino \t V - Vespertino \t N - Noturno")
x = input("Digite o período do dia: ")

if x == 'M' or x == 'm':
    print("Bom dia!")

elif x == 'V' or x == 'v':
    print("Boa Tarde!")

elif x == 'N' or x == 'n':
    print("Boa Noite!")

else:
    print("Entrada Inválida")
