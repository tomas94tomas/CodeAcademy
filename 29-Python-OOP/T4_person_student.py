# T4_person_student.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

if __name__ == "__main__":
    p = Person("John", 40)
    s = Student("Alice", 20, "A")
    print(f"Person: {p.name}, {p.age}")
    print(f"Student: {s.name}, {s.age}, {s.grade}")
