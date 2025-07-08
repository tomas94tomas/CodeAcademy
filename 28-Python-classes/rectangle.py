class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == "__main__":
    r1 = Rectangle(3, 4)
    print("Area:", r1.area())
    print("Perimeter:", r1.perimeter())
