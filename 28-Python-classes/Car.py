class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model} ({self.color})")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} ({self.color})"

    def __repr__(self):
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year}, color='{self.color}')"

if __name__ == "__main__":
    c = Car("Audi", "A7", 2020, "black")
    c.display_info()
    print(c)         # Calls __str__
    print(repr(c))   # Calls __repr__
