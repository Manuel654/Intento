class Person:
    def __init__(self, rut=0):
        self.rut = rut

    @property
    def rut(self):
        return self.__rut

    @rut.setter
    def rut(self, value):
        if value < 0:
            raise ValueError("This RUT is impossible")
        self.__rut = value



    