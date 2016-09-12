print(
    """
CGI = Common Gateway Interface = 'Imagens geradas por computador'

Consiste numa importante tecnologia que permite gerar páginas 
dinâmicas, permitindo a um navegador passar parâmetros para um 
programa alojado num servidor web. Assim, designam-se por scripts
CGI os pequenos programas que interpretam esses parâmetros e geram 
a página depois de os processar.

Embora a linguagem tipicamente associada aos CGI seja o Perl, o CGI
foi concebido de forma a ser independente da linguagem utilizada. 
Atualmente tecnologias como ASP.NET, PHP, Python e Ruby continuam a
utilizar a especificação.

EXEMPLOS: Django, App Engine, CherryPy, e Zope
    """
)

print(
    """
O processo de comunicação do servidor envolve as seguintes etapas
Envio
Exemplo:
1) Você faz preenche um cadastro no site
2) Você clica no botão 'cadastrar'
3) Browser manda suas informações através da internet para o servidor
   especificado, para isso bytes são enviados por meio de sockets
4) Um programa HTTP, funcionando constantemente, recebe as informações

Processamento
1) Programa HTTP recebe os bytes e decide o que fazer dado o que foi
   requisitado
2.1) Se o URL requisitado pelo browser for de extensão html, então o
     servidor devolverá a página
2.2) Se o URL requisitado for executavel (extanção .cgi, .py, ...) o 
     HTTP irá iniciar o programa no servidor para processar o
     requerimento e redirecionar os dados recebidos pelo browser para
     o programa
3) O programa iniciado irá lidar com o que foi requisitado

Resposta
O script CGI devolve o que foi processado no formato de uma página
html para o browser. Para isso o programa HTTP está conectado com
um socket do browser, e esse socket é definido como a saída padrão
para o programa CGI. 
    """
)

print(
    """
Para que possamos trabalhar com programação CGI antes de mais nada
é preciso configurar um servidor. Se você já tiver um servidor
configurado você pode utiliza-lo, senão é preciso configura-lo.
Você pode criar uma máquina apenas para rodar o servidor ou utilizar
o seu próprio computador e configurar o servidor nele. Os tutoriais
abaixo (também contidos na descrição do video) explicam como fazer
essas configurações:

Configurar Server Linux:
--> Ubuntu: https://www.digitalocean.com/community/tutorials/como-instalar-a-pilha-linux-apache-mysql-php-lamp-no-ubuntu-14-04-pt
--> Mint: http://community.linuxmint.com/tutorial/view/486
--> Debian: https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-debian
--> Fedora: https://www.digitalocean.com/community/tutorials/how-to-install-lamp-linux-apache-mysql-php-on-fedora
https://www.linux.com/community/blogs/129-servers/757148-configuring-apache2-to-run-python-scripts

Configurar Server Windows
--> http://www.wampserver.com/en/

Configurar Server MAC
--> http://jason.pureconcepts.net/2014/11/install-apache-php-mysql-mac-os-x-yosemite/

Criar Servidor Linux
https://www.youtube.com/watch?v=a5afUWHiZFs
https://www.youtube.com/watch?v=R8NeO5eAmJ8

Criar Servidor Windows
https://www.youtube.com/watch?v=AvODbkCZ9oM

Criar Servidor MAC
https://www.youtube.com/watch?v=LtGYm_qkjOg
    """
)

print(
    """
Alternativamente, utilizaramos o script http-server.py para simular
o uso de um servidor HTTP para evitar problemas de compatibilidade
e dores de cabeça durante a configuração.
    """
)
