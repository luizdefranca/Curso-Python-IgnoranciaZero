"""
Defina uma nova classe ObjetoGráfico subclasse de object, cujos atributos são:
    cor_de_preenximento --> inteiro
    preenxida --> bool
    cor_de_contorno --> inteiro

Escreva três classes:
    Retangulo --> Atributos: base e altura
    Circulo --> Atributos: raio
    Triangulo --> Atributos: base e altura

Subclasses da classe ObjetoGráfico que possuam todas métodos area e perimetro  
"""

class ObjetoGrafico(object):
    def __init__(self, cor_de_preenximento, preenxida, cor_de_contorno):
        self.cor_de_preenximento = cor_de_preenximento
        self.preenxida = preenxida
        self.cor_de_contorno = cor_de_contorno


class Retangulo(ObjetoGrafico):
    def __init__(self, cor_de_preenximento, preenxida, cor_de_contorno, base, altura):
        super().__init__(cor_de_preenximento, preenxida, cor_de_contorno)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base*self.altura
    def perimetro(self):
        return 2*(self.base + self.altura)

class Triangulo(ObjetoGrafico):
    def __init__(self, cor_de_preenximento, preenxida, cor_de_contorno, base, altura):
        super().__init__(cor_de_preenximento, preenxida, cor_de_contorno)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base*self.altura

    def perimetro(self):
        #ops! falha minha
        pass
from math import pi
class Circulo(ObjetoGrafico):
    def __init__(self, cor_de_preenximento, preenxida, cor_de_contorno, raio):
        super().__init__(cor_de_preenximento, preenxida, cor_de_contorno)
        self.base = raio

    def area(self):
        return pi*self.raio*self.raio

    def perimetro(self):
        return 2*pi*self.raio




