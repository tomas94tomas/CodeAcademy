# T3_shapes_area.py

import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == "__main__":
    r = Rectangle(4, 5)
    c = Circle(3)
    print("Rectangle area:", r.area())
    print("Circle area:", c.area())
