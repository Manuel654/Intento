from circle import Circle
from rectangle import Rectangle
my_circle = Circle(3)
print(my_circle.area())
print(my_circle.perimeter())

my_rectangle = Rectangle(3,4)

print (my_rectangle.area())
print (my_rectangle.perimeter())

figures = []
figures.append(Circle(3))
figures.append(Circle(4))
figures.append(Rectangle(3,4))
figures.append(Rectangle(4,4))

for figure in figures:
    print(figure.area())
    print(figure.perimeter())
# como todos son figuras se puede hacer un for con el método área.

