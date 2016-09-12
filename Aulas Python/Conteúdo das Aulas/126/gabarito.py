"""
Faça uma "fabrica decoradora" que retorna um decorador que decora funções com um único argumento. A fábrica deverá receber um argumento, um
tipo, e retornar um decorador em que a função verifica se o argumento passado é do tipo correto, senão levanta um TypeError.
"""

def decorador(função, tipo):
    def nova_função(arg):
        if type(arg) != tipo:
            raise TypeError
        else:
            return função(arg)
    return nova_função
