"""
Processo = programa
subprocesso = execução de código dentro do pograma
subprocess = Alternativa ao os.popen --> largado desde o python 2.6
subprocess.call = executa o comando --> os.system
subprocess.check_call = checa a saída do comando, e se houver erro levanta excessão
subprocess.check_output = devolve a saída do comando
subprocess.Popen(args, bufsize=0, stdin=None, stdout=None, stderr=None, preexec_fn=None, 
                 shell=False) 

args = Sequência de argumentos do programa
shell = Mesma regra de call
preexec_fn = Chama programa antes da execução
std-out/in/err = direciona a saída da execução
"""

import subprocess, sys

print("Vamos ler os arquivos do diretório")
if 'win' in sys.platform:
    subprocess.call(['dir'], shell = True)
else:
    subprocess.call(['ls', '-l'])
input()

print('O argumento shell tem de ser true no windows para')
print("executar programas construídos internamente, como type,")
print("dir, entre outros. Um programa normal como python não")
print("possuí necessidade deste argumento")
input()

print("No unix, por outro lado, o shell = false (padrão) indica")
print("que o comando será executa pelo os.execvp (veremos mais a")
print("frente no curso), quando shell = True o comando é executado")
print("na própria linha de comando")
input()

print("Vamos checar a saída de cat/type hello.py")
if 'win' in sys.platform:
    subprocess.check_call(["type", "hello.py"], shell = True)
else:
    subprocess.check_call(["cat","hello.py"])
input()

print("Vamos checar a saída de cat/type nao_existe.py")
if 'win' in sys.platform:
    try:
        subprocess.check_call(["type", "nao_existe.py"], shell = True)
    except Exception as E:
        print(E)
else:
    try:
        subprocess.check_call(["cat","nao_existe.py"])
    except Exception as E:
        print(E)
input()

print("Vamos armazenar a saída de cat/type hello.py")
if 'win' in sys.platform:
    o = subprocess.check_output(["type", "hello.py"], shell = True)
else:
    o = subprocess.check_output(["cat","hello.py"])
print("Saída:", o)
input()

print("O subprocess.Popen foi feito para ser um substituto de os.popen")
print("Ele funciona de maneira semelhante, porém um pouco mais complexo")
print("Por exemplo, a execução de os.popen('python3 hello.py').read() é")
print("Equivalente a escrever: ")
print("subprocess.Popen('python3 hello.py', stdout=subprocess.PIPE, shell = True).stdout.read()")
input()

print("Assim como o os.popen, o subprocess.Popen também retorna um objeto")
print("Capaz de lidar com os resultados da execução")
input()

print("Vamos criar o subprocess descrito acima e armazenar sua saída numa variável")
p = subprocess.Popen('python3 hello.py', stdout=subprocess.PIPE, shell = True)
input()

print("Vamos ver alguns detalhes de Popen: ")
input()

print("communicate = Permite mandar um input para o processo ou receber data dele")
print(p.communicate())
input()

print("Veja que communicate retorna uma tupla, a primeira é o resultado que")
print("fica na stdout, e a segunda é o stderr (None porque não houve erro na execução)")
input()

print("Depois faremos usaremos o communicate no Popen colocando o valor 42")
print("Veja o resultado da execução (temos de recria-lo para hello-2.py)")
print("Para tanto nosso subprocess necessitará de não apenas um stdout especificada como tambem uma stdin")
p = subprocess.Popen(['python3', 'hello-2.py'], stdin = subprocess.PIPE)
input()

print("Ai sim podemos chamar o communicate com um valor de input")
print("Detalhe: Valor de entrada deve estar em Bytes")
p.communicate(b'42')
input()
