"""
Threads não rodam realmente em paralelo a não ser que você
tenha várias CPUs, o que realmente acontece é que o sistema
operacional escolhe entre as tarefas a serem executadas aquela
a ser executada, e vai trocando entre as threads. O seu sistema
operacional faz isso tçao rápido que você tem a ilusão de que
as threads estão sendo executadas em paralelo. Esse processo
é chamado multiplexing.

Porém podemos fazer o python selecionar as tarefas a serem
executadas até todas serem completadas. Servidores podem
aplicar essa tpecnica para lidar com múltiplos clientes
ao mesmo tempo sem utilizar threads ou forks. 

Para fazer isso usamos o módulo 'select' da biblioteca padrão.
"""

