import urllib.request
import urllib.parse
import urllib.error

print(
"""
urllib permite que acessemos sites na internet, além
de poder acessar arquivos e realizar pedidos a determinados
domínios.
"""
)

input()

# Requisita que se abra um website
google = "https://www.google.com"
pagina = urllib.request.urlopen(google)

# A página é como um objeto file, por isso
# podemos usar métodos semelhantes como o read
# para exibir todo o conteúdo da página
print(pagina.read())

input()

print(
"""
Mais do que isso podemos até mesmo reter uma página
da web ou alguma imagem
"""
)

input()

# f = open('00000001.jpg','wb')
# f.write(urllib.request.urlopen('http://www.gunnerkrigg.com//comics/00000001.jpg').read())
# f.close()

urllib.request.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")

input()

print(
"""
Além de podermos obter o HTML que contém uma determinada
página da web podemos fazer requirementos a um determinado
domínio. Por exemplo, é possível realizar uma busca no google
utilizando https://www.google.com/?#q=pesquisa. Da mesma
forma podemos fazer pesquisas usando urllib.parse+urllib.request
"""
)

input()

# Canal sentdex

# Vamos acessar o site python programming e realizar uma busca
url = 'http://pythonprogramming.net'

# Nesta busca vamos buscar pela palavra 'basics' utilizando o
# método search
valores = {'s' : 'basics',
          'submit' : 'Search'}

# Em seguida vamos processar e codificar o nosso requerimento
data = urllib.parse.urlencode(valores)
data = data.encode('utf-8')

# Em seguida vamos efetivamente requirir uma resposta
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)

# Vamos ler e imprimir essa resposta
respData = resp.read()
print(respData)

input()

print(
"""
Entretanto a maioria dos websites não são tão abertos
assim, por uma questão de segurança
"""
)

input()

try:
    pagina = urllib.request.urlopen('http://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol=JPASSOCIAT&fromDate=1-JAN-2012&toDate=1-AUG-2012&datePeriod=unselected&hiddDwnld=true')
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())  

input()

print(
"""
Ao invéz disso para realizar um requerimento desse jeito
nós precisamos mandar informações para o website sobre nós
como o nosso endereço, o browser que estamos usando.
Todas essas informações ficam contidas num bloco de informações
chamado 'headers'
"""
)

try:
    google = "https://www.google.com.br/?#q=pesquisa"

    # Vamos colocar nossas informações dentro do header
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    # Vamos novamente realizar um requerimento, entretanto
    # Desta vez vamos passar os headers para realiza-lo
    req = urllib.request.Request(google, headers = headers)

    # Vamos obter uma resposta
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    # E desta vez vamos colocar toda a informação dentro
    # de um arquivo
    arq = open('com_headers.html','w')
    arq.write(str(respData))
    arq.close()

except Exception as e:
    print(str(e))

input()
