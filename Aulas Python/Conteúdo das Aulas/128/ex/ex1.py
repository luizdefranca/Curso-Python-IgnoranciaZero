"""
Lembra-se do decorador de tag html da aula de decoradores de funções (veja abaixo)?
Então, escreva 2 funções decoradoras, uma usando o método format
e outro usando o objeto Template do módulo string
"""

def tags(nome_tag):
    def tags_decorador(func):
        def nova_func(num1, num2):
            return "<" + nome_tag + ">" + func(num1, num2) + "</" + nome_tag + ">"
        return nova_func
    return tags_decorador

@tags("p")
def devolve_trecho(num1, num2):
    return "Resultado: %g"%(num1 * num2)

print("devolve_trecho(2,3) =", devolve_trecho(2,3))
