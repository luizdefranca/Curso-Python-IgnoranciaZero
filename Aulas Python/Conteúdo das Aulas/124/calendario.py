class Calendario(object):

    meses = (31,28,31,30,31,30,31,31,30,31,30,31)

    def anobissexto(ano):
        """ 
        Se o ano é bissexto retorna true, senão
        retorna false
        """

        if ano % 4 == 0:
            if ano % 100 == 0:
                # divisivel por 4 e por 100
                if ano % 400 == 0:
                    bissexto = True
                else:
                    bissexto = False
            else:
                # divisivel por 4 mas nao por 100
                bissexto = True
        else:
            # não divisivel por 4
            bissexto = False

        return bissexto


    def __init__(self, d, m, a):
        """
        Dia mês e ano são inteiros e ano deve ter 4 digitos
        """

        self.configura_Calendario(d,m,a)


    def configura_Calendario(self, d, m, a):
        """
        Dia mês e ano são inteiros e ano deve ter 4 digitos
        """

        if type(d) == int and type(m) == int and type(a) == int:
            self.__dias = d
            self.__meses = m
            self.__anos = a
        else:
            raise TypeError("Dia mês e ano são inteiros!")


    def __str__(self):
        return "%.2i/%.2i/%.4i"%(self.__dias, self.__meses, self.__anos)



    def avança(self):
        """
        Avança para próxima data
        """

        max_dias = Calendario.meses[self.__meses-1]
        if self.__meses == 2 and Calendario.anobissexto(self.__anos):
            max_dias += 1
        if self.__dias == max_dias:
            self.__dias= 1
            if self.__meses == 12:
                self.__meses = 1
                self.__anos += 1
            else:
                self.__meses += 1
        else:
            self.__dias += 1


if __name__ == "__main__":
    x = Calendario(31,12,2012)
    print(x, end=" ")
    x.avança()
    print("Depois do avanço: ", x)
    print("2012 é bissexto:")
    x = Calendario(28,2,2012)
    print(x, end=" ")
    x.avança()
    print("Depois do avanço: ", x)
    x = Calendario(28,2,2013)
    print(x, end=" ")
    x.avança()
    print("Depois do avanço: ", x)
    print("1900 não bissexto: divisivel por 100 mas não por 400 ")
    x = Calendario(28,2,1900)
    print(x, end=" ")
    x.avança()
    print("Depois do avanço: ", x)
    print("2000 é bissexto:")
    x = Calendario(28,2,2000)
    print(x, end=" ")
    x.avança()
    print("Depois do avanço: ", x)
