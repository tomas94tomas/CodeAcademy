# T6_company_hierarchy.py

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_role(self):
        return "Employee"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_role(self):
        return "Manager"

class Engineer(Employee):
    def __init__(self, name, salary, specialty):
        super().__init__(name, salary)
        self.specialty = specialty

    def get_role(self):
        return "Engineer"

class Intern(Employee):
    def __init__(self, name, salary, duration_months):
        super().__init__(name, salary)
        self.duration_months = duration_months

    def get_role(self):
        return "Intern"

if __name__ == "__main__":
    m = Manager("Tom", 5000, 10)
    e = Engineer("Anna", 3000, "DevOps")
    i = Intern("Jake", 800, 6)
    for emp in [m, e, i]:
        print(f"{emp.get_role()}: {emp.name}, {emp.salary}")
