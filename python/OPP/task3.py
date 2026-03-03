class Employee:
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    def display_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_count(cls):
        print(f"Total Employees: {cls.counter}")


# Crear empleados
emp1 = Employee("Ana", 3000)
emp2 = Employee("Luis", 4000)

emp1.display_employee()
emp2.display_employee()

Employee.display_count()


print("Base classes:", Employee.__base__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)