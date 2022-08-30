from figure import Figure
from math import pi

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi*self.radius ** 2
    
    def perimeter(self):
        return pi*2*self.radius