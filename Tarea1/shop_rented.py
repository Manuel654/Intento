from shop import Shop

class Rented(Shop):
    def __init__(self, type, condition, rut, rent):
        self.type = type
        self.condition = condition
        self.rut = rut
        self.rent = rent

    @property
    def rut(self):
        return self.__rut

    @rut.setter
    def rut(self, value):
        if value < 0:
            raise ValueError("This RUT is impossible")
        self.__rut = value