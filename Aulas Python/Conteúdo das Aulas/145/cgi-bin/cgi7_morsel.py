#!/usr/bin/python
# coding: UTF-8

import Cookie
import cgitb; cgitb.enable()
import os
from time import strftime
from datetime import datetime

cookstr = os.environ.get("HTTP_COOKIE")

if not cookstr:
    ola = '<p>Primeira Visita, ou os cookies estao desabilitados</p>\n'

    cookies = Cookie.SimpleCookie()

    # Toda vez que que uma nova chave é criada para um objeto cookie, um
    # objeto morsel também é criado para manter o valor dessa chave. Cada
    # instância de morsel também possuí algumas chaves pré definidas, são
    # elas: expires, path, commnent, domain, max-age, secure e version 
    cookies['user'] = 'Bruno'
    cookies['lastvisit'] = str(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

    # Vamos modificar o morsel para lastvisit para entender o que cada uma 
    # de suas chaves significam

    # Expira o cookie em x segundos depois dele ser criado.
    # O padrão é que o cookie expire no momento em que o browser
    # é fechado. No caso abaixo o cookie só irá expirar depois
    # de 1 mês
    cookies['lastvisit']['expires'] = 30 * 24 * 60 * 60

    # Caminho no qual o cookie é valido.
    # Se for colocado como '/' será válido em todo o dominio.
    # O padrão é o caminho para o script executado.
    # cookies['lastvisit']['path'] = '/cgi-bin/'

    # O propósito do cookie a ser inspecionado pelo usuário caso
    # ele decida em deleta-lo ou não
    cookies['lastvisit']['comment'] = 'Mantem a data de ultimo acesso do usuario'

    # Dominio no qual o cookie é válido. Sempre comoça com um .
    # para ser acessível por todos subdominios
    # cookies['lastvisit']['domain'] = '.www.meusite.com.br'

    # Descarta o cookie x segundos depois de ser criado.
    # Não é suportado pela maioria dos browsers
    cookies['lastvisit']['max-age'] = 30 * 24 * 60 * 60

    # secure não tem valor. Se for configurado direciona o usuario
    # agente para usar apenas (não especificado) meios de segurança para
    # contactar a origem do servidor toda vez que este cookie for enviado
    # de volta por este
    # cookies['lastvisit']['secure'] = ''

    # um inteiro decimal, que identifica a vesão das especificações
    # do estado de manejamento do cookie
    # cookies['lastvisit']['version'] = 1

    # Impriremos os dados do cookie criado
    print(cookies)
    ola += '<p>' + str(cookies) + '</p>'

    # Criaremos um paragrafo com a informação do usuário
    ola += '<p>O seu nome sera... %s</p>' % cookies['user'].value

    for morsel in cookies:
       ola += '<p>' + str(morsel) + ' = ' + str(cookies[morsel].value)
       ola += '<div style="margin:-1em auto auto 3em;">'
       for key in cookies[morsel]:
          ola += str(key) + ' = ' + str(cookies[morsel][key]) + '<br />'
       ola += '</div></p>'

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
