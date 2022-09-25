zero = -273.15
class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature
    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self, value):
        if value>zero:
            self.__temperature = value
        else:
            raise ValueError('La temperatura debe ser mayor a -273.15')