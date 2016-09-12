from relogio import Relogio
from calendario import Calendario


class Horario(Relogio, Calendario):
    """ 
	Classe implementa um relogio integrado com calendario           
    """

    def __init__(self, dia, mes, ano, hora, minuto, segundo):
        Relogio.__init__(self,hora, minuto, segundo)
        Calendario.__init__(self,dia, mes, ano)


    def tick(self):
        """
        Avança o relógio em 1 segundo
        """
        hora_anterior = self.horas
        Relogio.tick(self)
        if (self.horas < hora_anterior): 
            self.avança()

    def __str__(self):
        return Calendario.__str__(self) + ", " + Relogio.__str__(self)


if __name__ == "__main__":
    x = Horario(31,12,2013,23,59,59)
    print("Um tick de ",x, end=" ")
    x.tick()
    print("para ", x)

    x = Horario(28,2,1900,23,59,59)
    print("Um tick de ",x, end=" ")
    x.tick()
    print("para ", x)

    x = Horario(28,2,2000,23,59,59)
    print("Um tick de ",x, end=" ")
    x.tick()
    print("para ", x)

    x = Horario(7,2,2013,13,55,40)
    print("Um tick de ",x, end=" ")
    x.tick()
    print("para ", x)
