# T1_person_encapsulation.py

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        self.__age = age

if __name__ == "__main__":
    p = Person("Tom", 30)
    print("Name:", p.get_name())
    print("Age:", p.get_age())
    p.set_name("Anna")
    p.set_age(25)
    print("Updated Name:", p.get_name())
    print("Updated Age:", p.get_age())
