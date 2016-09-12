"""
Lembra-se do decorador de tag html da aula de decoradores de funções (veja abaixo)?
Então, escreva 2 funções decoradoras, uma usando o método format
e outro usando o objeto Template do módulo string
"""
from string import Template

def tags(nome_tag):
    def tags_decorador(func):
        def nova_func(num1, num2):
            return "<" + nome_tag + ">" + func(num1, num2) + "</" + nome_tag + ">"
        return nova_func
    return tags_decorador

def tags_format(nome_tag):
    def tags_decorador(func):
        def nova_func(num1, num2):
            return "<{0}>{1}</{0}>".format(nome_tag, func(num1, num2))
        return nova_func
    return tags_decorador

def tags_template(nome_tag):
    def tags_decorador(func):
        def nova_func(num1, num2):
            t = Template("<$tag>$res</$tag>")
            return t.substitute(tag = nome_tag, res = func(num1, num2))
        return nova_func
    return tags_decorador

@tags("p")
def devolve_trecho1(num1, num2):
    return "Resultado: %g"%(num1 * num2)

@tags_format("p")
def devolve_trecho1(num1, num2):
    return "Resultado: %g"%(num1 * num2)

@tags_template("p")
def devolve_trecho1(num1, num2):
    return "Resultado: %g"%(num1 * num2)

print("devolve_trecho1(2,3) =", devolve_trecho1(2,3))
print("devolve_trecho2(2,3) =", devolve_trecho1(2,3))
print("devolve_trecho3(2,3) =", devolve_trecho1(2,3))
