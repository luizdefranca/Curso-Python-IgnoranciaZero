#Época = Tempo em que se começou a medir o tempo no computador (para Unix, 1970)
#Time Zone = Fuso horário = representa a diferença de horário com relação a um fuso tomado como padrão(greenwich)
#UTC = Tempo universal coordenado = fuso horário de referência a partir do qual se calculam todas as outras zonas horárias do mundo
#18:24
#DST = Daylight Saving Time = Horário de Verão
#+1
#Tempo Local = Tempo no fuso e com o DST apropriado
#16:24

import time

#Dia da Semana, mês, dia, horário e ano
print(time.asctime())

#Classe que representa o tempo
tempo = time.struct_time()
"""
0	tm_year	    (por exemplo, 1993)
1	tm_mon	    range [1, 12]
2	tm_mday	    range [1, 31]
3	tm_hour	    range [0, 23]
4	tm_min	    range [0, 59]
5	tm_sec	    range [0, 61]
6	tm_wday	    range [0, 6], Segunda-feira é 0
7	tm_yday	    range [1, 366]
8	tm_isdst    0, 1 or -1; see below
N/A	tm_zone	    nome da timezone
N/A	tm_gmtoff   Variação de segundos a leste do UTC
"""

#Fornece uma tupla
#ano, mês, dia, horas, minutos, segundos, dia da semana, dia do ano, DST
print(time.localtime())

#Tempo em segundos desde de o começo de uma certa contagem de tempo
print(time.time()) #--> Bom para medir intervalos de tempo

#Tempo de espera em segundos
time.sleep(3)

#Tempo de execução do programa
#não conta tempo de sleep
print(time.process_time())

#Retorna uma struct_time do tempo local do tempo desde a época passados n segundos
print(time.localtime(time.time()))

#Retorna uma struct_time do tempo em UTC desde a época passados n segundos
print(time.gmtime(time.time()))

#Formata o tempo a partir de um struct_time
print(time.asctime(time.localtime(time.time())))
