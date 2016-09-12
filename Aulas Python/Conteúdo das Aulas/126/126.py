#Decoradores de Funções

print("Algumas funções construídas por um programador")
print("pode sofrer modificações ao longo do desenvolvimento")
print("do aplicativo, o que significa que tudo o que um")
print("programador escreve deve estar apto a sofre modificações.")
print("Em python existe uma forma simples de adicionar funcionalidades")
print("a uma dada função a partir de outra função DECORADORA.")
input()

print("A função decoradora recebe uma função qualquer")
print("e devolve uma outra função (pode ser até a mesma)")
print("modificada.")
input()

print("Por exemplo, suponhamos que tenhamos escrito")
print("uma função na qual queiramos escrever uma página html")
print("cada vez que chamamos a função ela devolve um trecho")
print("da página. Mas nós queremos mudar o tipo de saída,")
print("isto é queremos colocar um paragrafo, ou um título")
print("ou até mesmo uma tabela. Para isso vamos usar decoradores")
print("especiais.")
input()

print("Então vamos supor nossa função abaixo:")
print("""
def devolve_trecho(num1, num2):
    return "Resultado: %g"%(num1 * num2)
""")
def devolve_trecho(num1, num2):
    return "Resultado: %g"%(num1 * num2)
input()

print("Para escrever um decorador de paragrafo")
print("poderíamos escrever:")
def p_decorador(func):
    def nova_func(num1, num2):
        return "<p>" + func(num1, num2) + "</p>"
    return nova_func
print("""
def p_decorador(func):
    def nova_func(num1, num2):
        return "<p>" + func(num1, num2) + "</p>"
    return nova_func
""")
input()

print("Então poderíamos fazer:")
print("devolve_trecho = p_decorador(devolve_trecho)")
devolve_trecho = p_decorador(devolve_trecho)
print("para modificar a função devolve_trecho.")
print("Assim, se fizessemos: devolve_trecho(2, 3)")
print("teríamos:")
print(devolve_trecho(2, 3))
input()

print("Python possuí uma sintaxe um pouco mais sofisticada")
print("Que permite comprimir o código, que seria:")
print("""
def p_decorador(func):
    def nova_func(num1, num2):
        return "<p>" + func(num1, num2) + "</p>"
    return nova_func

@p_decorador
def devolve_trecho(num1, num2):
    return "Resultado: %g"%(num1 * num2)
""")
input()

print("Em essência o código indica a mesma coisa que:")
print("""
def p_decorador(func):
    def nova_func(num1, num2):
        return "<p>" + func(num1, num2) + "</p>"
    return nova_func

def devolve_trecho(num1, num2):
    return "Resultado: %g"%(num1 * num2)

devolve_trecho = p_decorador(devolve_trecho)
""")
print("de forma mais elegante.")
input()

print("Essa sintaxe é melhor porque poderíamos colocar vários")
print("decoradores para uma mesma função com o mesmo")
print("código, por exemplo: ")
print("""
def p_decorador(func):
    def nova_func(num1, num2):
        return "<p>" + func(num1, num2) + "</p>"
    return nova_func

def div_decorador(func):
    def nova_func(num1, num2):
        return "<div>" + func(num1, num2) + "</div>"
    return nova_func

def strong_decorador(func):
    def nova_func(num1, num2):
        return "<strong>" + func(num1, num2) + "</strong>"
    return nova_func

@p_decorador
@div_decorador
@strong_decorador
def devolve_trecho(num1, num2):
    return "Resultado: %g"%(num1 * num2)
""")

def p_decorador(func):
    def nova_func(num1, num2):
        return "<p>" + func(num1, num2) + "</p>"
    return nova_func

def div_decorador(func):
    def nova_func(num1, num2):
        return "<div>" + func(num1, num2) + "</div>"
    return nova_func

def strong_decorador(func):
    def nova_func(num1, num2):
        return "<strong>" + func(num1, num2) + "</strong>"
    return nova_func

@p_decorador
@div_decorador
@strong_decorador
def devolve_trecho(num1, num2):
    return "Resultado: %g"%(num1 * num2)

print("Temos devolve_trecho(2, 3) =", devolve_trecho(2, 3))
input()

print("Note que as funções decoradoras tem estruturas")
print("bastantes semelhantes, então o ideal seria")
print("escrever uma única função tag_decorador")
print("que recebece um argumento de forma a colocar a")
print("tag adequada.")
input()

print("Poderíamos escrever o seguinte:")
print("""
def tags(nome_tag):
    def tags_decorador(func):
        def nova_func(num1, num2):
            return "<" + nome_tag + ">" + func(num1, num2) + "</" + nome_tag + ">"
        return nova_func
    return tags_decorador

@tags("p")
def devolve_trecho(num1, num2):
    return "Resultado: %g"%(num1 * num2)
""")
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



