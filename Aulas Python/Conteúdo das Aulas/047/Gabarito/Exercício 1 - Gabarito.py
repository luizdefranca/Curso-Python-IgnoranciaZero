"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
a.	"Telefonou para a vítima?"
b.	"Esteve no local do crime?"
c.	"Mora perto da vítima?"
d.	"Devia para a vítima?"
e.	"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa
no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""
def main():
    perguntas = ['Telefonou para a vítima?', "Esteve no local do crime?",
                 "Mora perto da vítima?", "Devia para a vítima?",
                 "Já trabalhou com a vítima?"]
    classificação = ["Inocente", "Inocente", "Suspeita", "Cúmplice",
                     "Cúmplice", "Assassina"]
    cont = 0
    for pergunta in perguntas:
        resp = input(pergunta)

        if tudoMinusculo(resp) == 'sim':
            cont += 1

    print(classificação[cont])

def tudoMinusculo(palavra):
    minusculo = ""
    for char in palavra:
        if ord('A') <= ord(char) <= ord('Z'):
            char = chr(ord(char) - (ord('A') - ord('a')))

        minusculo += char

    return minusculo

main()
    
