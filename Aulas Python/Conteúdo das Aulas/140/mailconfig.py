"""
Configurações do usuário para varios programas envolvendo emails. Os scripts de
email recebem o nome do servidor e outros opções de configuração a partir deste
módulo
"""

#------------------------------------------------------------------------------
# (obrigatório) Servidor de POP3 e seu usuário
#------------------------------------------------------------------------------
servidor_pop = "pop.googlemail.com"
usuário_pop = "pedro.henrique.forli"

#------------------------------------------------------------------------------
# (obrigatório) Servidor de SMTP
# Veja o módulo smtpd para ver como rodar um servidor SMTP na sua máquina
#------------------------------------------------------------------------------
servidor_smtp = "smtp.gmail.com"
port_smtp = '587'

#------------------------------------------------------------------------------
# Informação pessoal usada pelos clientes para preencher o email;
# signature -- Pode ser uma string com três aspas, ou uma string vazia
# address -- Usada como valor inicial do campo "De:" se for diferente de nulo
#------------------------------------------------------------------------------
meu_endereço = 'PP4E@learning-python.com'
minha_assinatura = ('Thanks,\n'
                    '--Mark Lutz (http://learning-python.com, http://rmi.net/~lutz)')

#------------------------------------------------------------------------------
# (opcional) Pode ser utilizado para mandar para o servidor SMTP o usuário e
# e senha para poder ser autenticado
#------------------------------------------------------------------------------
usuário_smtp = "pedro.henrique.forli@gmail.com"
senha_smtp = ''
