# T5_shapes_perimeter.py

import math

class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    r = Rectangle(4, 5)
    c = Circle(3)
    print("Rectangle perimeter:", r.perimeter())
    print("Circle perimeter:", c.perimeter())
