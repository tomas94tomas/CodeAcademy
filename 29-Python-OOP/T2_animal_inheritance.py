# T2_animal_inheritance.py

class Animal:
    def speak(self):
        return "I don't know what sound I make"

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

if __name__ == "__main__":
    a = Animal()
    d = Dog()
    c = Cat()
    print("Animal:", a.speak())
    print("Dog:", d.speak())
    print("Cat:", c.speak())
