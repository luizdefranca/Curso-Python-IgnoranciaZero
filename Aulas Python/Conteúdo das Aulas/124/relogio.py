class Relogio(object):

    def __init__(self, hor, minutos, seg):
        """
        Os parâmetros horas, minutos e segundos são inteiros
        que devem satisfazer as seguintes inequações:
        0 <= h < 24
        0 <= m < 60
        0 <= s < 60
        """

        self.configura_Relogio(hor, minutos, seg)

    def configura_Relogio(self, hor, minutos, seg):
        """
        Os parâmetros horas, minutos e segundos são inteiros
        que devem satisfazer as seguintes inequações:
        0 <= h < 24
        0 <= m < 60
        0 <= s < 60
        """

        if type(hor) == int and 0 <= hor < 24:
            self.horas = hor
        else:
            raise TypeError("Horas são inteiros entre 0 e 23!")
        if type(minutos) == int and 0 <= minutos < 60:
            self.__minutos = minutos 
        else:
            raise TypeError("Minutos são inteiros entre 0 e 59!")
        if type(seg) == int and 0 <= seg < 60:
            self.__segundos = seg
        else:
            raise TypeError("Segundos são inteiros entre 0 e 59!")

    def __str__(self):
        return "%.2i:%.2i:%.2i"%(self.horas, self.__minutos, self.__segundos)

    def tick(self):
        """
        Faz o relógio adiantar em 1 segundo.

        Exemplos:
        >>> x = Relogio(12,59,59)
        >>> print(x)
        12:59:59
        >>> x.tick()
        >>> print(x)
        13:00:00
        >>> x.tick()
        >>> print(x)
        13:00:01
        """

        if self.__segundos == 59:
            self.__segundos = 0
            if self.__minutos == 59:
                self.__minutos = 0
                if self.horas == 23:
                    self.horas = 0
                else:
                    self.horas += 1
            else:
                self.__minutos += 1
        else:
            self.__segundos += 1


if __name__ == "__main__":
    x = Relogio(23,59,59)
    print(x)
    x.tick()
    print(x)
    y = str(x)
    print(type(y))
