#!/usr/bin/python
# coding: UTF-8

# OBS: O modulo para lidar com cookies utilizado geralmente
# é o http.cookies, por algum motivo quando eu tentava importar
# esse modulo eu esbarrava com um erro, que pode ser corrigido
# importando o modulo Cookie. Se alguem souber a causa ou como
# corrigir o erro, por favor escreva abaixo, você pode tentar
# utilizar o http.cookies, a única coisa que você terá de fazer
# é trocar todas as menções ao módulo Cookie por http.cookies
import Cookie
import cgitb; cgitb.enable()
import os
from time import strftime
from datetime import datetime

# O ambiente HTTP-COOKIE contem todos os cookies
# envidos pelo cliente
cookstr = os.environ.get("HTTP_COOKIE")

# Se por algum motivo não tiver nenhum cookie ou os cookies estiverem
# desabilitados
if not cookstr:
    ola = '<p>Primeira Visita, ou os cookies estão desabilitados</p>\n'

    # Iremos criar um novo cookie para enviar ao usuário
    cookies = Cookie.SimpleCookie()

    # Configuraremos o nome de usuário como sendo Bruno 
    cookies['user'] = 'Bruno'
    cookies['lastvisit'] = str(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
    print(cookies)

    # Impriremos os dados do cookie criado
    # print(cookies)
    ola += '<p>' + str(cookies) + '</p>'

    # Criaremos um paragrafo com a informação do usuário
    ola += '<p>O seu nome eh... %s</p>' % cookies['user']

else:
    ola = '<p>A Cookie string eh, "' + cookstr + '"</p>\n'

    # Podemos carregar o cookie a partir desse ambiente
    cookies = Cookie.SimpleCookie(cookstr)

    # Usando o método get podemos pegar o cookie que contem
    # as informações do usuário
    usercook = cookies.get("user")
    lastvisit = cookies.get("lastvisit")

    # Adicionamos o tempo da última visita
    ola +='<p> Sua ultima visita foi em ' + str(lastvisit.value) + '</p>\n'

    # Imprimiremos uma mensagem com bem-vindo de volta com
    # o nome obtido
    ola += '<p>Bem vindo de volta, %s</p>' % usercook.value

    # Recolocamos o cookie com o valor de last visit atualizado
    cookies['lastvisit'] = str(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
    print(cookies)

# Por fim nós imprimimos a página
# Iniciamos a impressão da página
print('Content-type: text/html\n')
print(ola)
