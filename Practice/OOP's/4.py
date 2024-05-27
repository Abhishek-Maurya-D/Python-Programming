# Define a Employee class with attributes role, department & salary. This class also has showDetails() method.

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.dept = department
        self.sal = salary

    def showDetails(self):
        print("Role : ", self.role)
        print("Department : ", self.dept)
        print("Salary : ", self.sal)

e1 = Employee("Accountant", "Finance", 36000)
e1.showDetails()


# Create an Engineer class that inherits properties from Employee & has additional attributes : name & age.

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 75000)

engg1 = Engineer("Elon Musk", 23)
print()
print(engg1.name)
print(engg1.age)
engg1.showDetails()