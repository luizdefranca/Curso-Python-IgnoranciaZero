"""
Veja o texto abaixo:

Querido [nome]

Eu gostaria de aprender a programar. Eu ouvi dizer que você
utiliza muito a linguagem [linguagem] -- isso é algo que
eu deveria considerar?

E, por sinal, o email [email] é o seu, correto?

[Cidade], [dia]

Pedro Forli

Crie uma forma de ao receber os dados necessários montar o texto
equivalente
"""

t = """
Querido {nome}

Eu gostaria de aprender a programar. I ouvi dizer que você
utiliza muito a linguagem {linguagem} -- isso é algo que
eu deveria considerar?

E, por sinal, o email {email} é o seu, correto?

{cidade}, {tempo}

Pedro Forli
"""

nome = input("Digite o nome do correspondente: ")
email = input("Digite o email do correspondente: ")
linguagem = input("Digite a linguagem de programação do correspondente: ")
cidade = input("Digite sua cidade: ")
import time
print(t.format(tempo = time.asctime(), nome = nome, linguagem = linguagem, email = email, cidade = cidade))
