from abc import ABC, abstractmethod
#clase abstracta
#con abstractmethod se les obliga a los herederos a tener este método
class Figure(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

