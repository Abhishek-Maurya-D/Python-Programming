# Static Methods
# Methods that don't use the self parameter (work at class level)

# Decorators allow us to wrap another function in order
# to extend the behaviour of the wrapped function, without
# permanently modifying it

class Student:
    def __init__(self, fullname):
        self.name = fullname

    @staticmethod
    def hello():
        print("Hello")

    def print_hello(self):
        print("Hello", self.name)

s1 = Student("Abhishek")
s1.print_hello()
s1.hello()