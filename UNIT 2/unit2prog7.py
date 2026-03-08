# Manager Class Example (Multiple Inheritance)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def show_employee(self):
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary, team):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)

        # Manager specific attribute
        self.team = team

    def show_manager_details(self):
        print("\nManager Details")
        print("----------------")
        self.show_person()
        self.show_employee()
        print("Team Managed:", self.team)


# Creating object
m1 = Manager("Rahul", 30, "EMP245", 50000, "Software Development")

# Calling method
m1.show_manager_details()