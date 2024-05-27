# Methods 
# Methods are functions that belong to objects.

# creating class
class Student:
    def __init__(self, fullname):
        self.name = fullname

    def hello(self):
        print("Hello", self.name)

s1 = Student("Abhishek")
s1.hello()