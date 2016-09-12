print("Programação para Internet")

input()

print("Python é muito usado em aplicativos")
print("de internet, sendo extensamente usado")
print("pela engine de busca da google, o youtube")
print("dropbox entre outros")

input()

print("Existem muitas ferramentas em python para")
print("se programar para internet, entre elas")
print("a Google App Engine, Django e o Jython")
print("entretanto pretendo dar somente uma introdução")
print("aos módulos que vem na biblioteca básica de python")
print("uma vez que um curso inteiro poderia ser montado")
print("somente para discutir esse tópico")

input()

print("Quanto mais conhecimento você tiver de")
print("como a internet funciona mais facilmente")
print("este tópico do curso será digerido")

input()

print("Sockets")

input()

print("São interfaces programáveis de comunicação")
print("entre softwares que podem estar rodando")
print("em computadores distintos na rede")
print("Eles permitem transferir strings em bytes")
print("de um processo para outro e é a base da maioria")
print("dos protocolos de alto nível, como FTP, páginas")
print("da Web, e email")

input()

print("A comunicação entre diferentes computadores")
print("deve ser feita tendo o endereço de um computador")
print("e o canal de comunicação a ser usado, ou seja,")
print("o nome da máquina (endereço de IP ou nome do domínio), ")
print("e o port number (número de identificação da conversa)")
print("A combinação de ambos fornecerá um dialog na Net")

input()

print("Toda a comunicação na internet é baseada em protocolos")
print("que rodam por cima dos Sockets. São eles que padronizam")
print("o formato da menssagem (estrutura para os bytes a serem")
print("trocados) e a port number do socket (entre 0 e 65535)")

input()

print("""
Port Number 0-1023 --> Protocolos padrões

Protocolo   Função comum                  Port number    Modulo do Python

HTTP        Páginas de WebWeb pages       80             http.client , 
                                                         http.server

NNTP        Novidades Usenet              119            nntplib

FTP         Tranferência de Arquivos      20             ftplib

FTP         Controle de transferência     21             ftplib
            de arquivos

SMTP        Mandar email                  25             smtplib

POP3        Buscar email                  110            poplib

IMAP4       Buscar email                  143            imaplib

Finger      Informacional                 79             n/a

SSH         Linhas de Comando             22             n/a

Telnet      Linhas de Comando             23             telnetlib
""")

input()

print("A estrutura cliente servidor")
print("Para boa parte dos serviços a Net utiliza a")
print("estrutura cliente-servidor. O servidor é aquele")
print("que está continuamente executando e esperando uma")
print("entrada, e o cliente são aqueles que tentam se")
print("comunicar com o servidor")

input()

print("Vamos ver agora uma pequena demonstração da estrutura")
print("cliente servidor usando sockets")

input()

print("Não há nada que nos impeça de realizar conexões")
print("usando as ports padrões (0-1023)")

from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('pop.secureserver.net', 110))
# Conversa com pop email server
print(sock.recv(70))
sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('learning-python.com', 21))
# Conversa com server FTP
print(sock.recv(70))
sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('www.python.net', 80))
# Conversa com server HTTP
sock.send(b'GET /\r\n')
# Recebe a página como resposta
print(sock.recv(70))
print(sock.recv(70))

input()
