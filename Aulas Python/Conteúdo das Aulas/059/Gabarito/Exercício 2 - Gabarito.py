"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e
calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe
as medidades de um local. Depois, deve criar um objeto com as medidas e calcular
a quantidade de pisos necessárias para o local.
"""

class Retangulo(object):
    def __init__(self):
        self.base = 0
        self.altura = 0

    def MudaLados(self, b, h):
        self.base = b
        self.altura = h

    def RetornaLados(self):
        return self.base, self.altura

    def Area(self):
        return self.base*self.altura

    def Perimetro(self):
        return 2*(self.base + self.altura)


largura = float(input("Digite a largura do local: "))
comprimento = float(input("Digite o comprimento do local: "))

piso = Retangulo()

lag_piso = float(input("Digite a largura do piso: "))
com_piso = float(input("Digite o comprimento do piso: "))

piso.MudaLados(lag_piso, com_piso)

areaTotal = largura*comprimento
num_de_pisos = round(areaTotal/piso.Area())

print("Serão necessários %i pisos."%num_de_pisos)

