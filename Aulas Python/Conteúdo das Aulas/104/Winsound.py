import winsound

#Dá um beep numa frequência determinada por um período determinado
winsound.Beep(300, 1000)

#Coloca uma música qualquer carregada em file com as flags determinadas
winsound.PlaySound("teste.wav", winsound.SND_FILENAME|winsound.SND_PURGE|winsound.SND_NODEFAULT)

#Flags
#SND_FILENAME = O som é o som passado como parâmetro
#SND_ALIAS = O som é um som do sistema
"""
'SystemAsterisk'	 Asterisk
'SystemExclamation'	 Exclamation
'SystemExit'	     Exit Windows
'SystemHand'	     Critical Stop
'SystemQuestion'	 Question
"""
#SND_LOOP = Toca o som repetidamente
#SND_PURGE = Para todas as instâncias do som
#SND_NODEFAULT = Caso o som não seja encontrado, não toca som default do sistema
#SND_NOSTOP = não interrompe sons tocando
#SND_ASYNC = Permite que a música toque no fundo

#Manda um beep de msg
winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
#winsound.MessageBeep(winsound.MB_ICONASTERISK)
#winsound.MessageBeep(winsound.MB_ICONHAND)
#winsound.MessageBeep(winsound.MB_ICONQUESTION)
#winsound.MessageBeep(winsound.MB_OK)
#MB_ICONASTERISK = Play the SystemDefault sound.
#MB_ICONEXCLAMATION = Play the SystemExclamation sound.
#MB_ICONHAND = Play the SystemHand sound.
#MB_ICONQUESTION = Play the SystemQuestion sound.
#MB_OK = SstemDefault sound.
