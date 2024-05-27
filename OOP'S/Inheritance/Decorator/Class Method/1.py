# Class Method
# A class method is bound to the class & receives the class as an implicit first argument.ArithmeticError
# Note - Static method can't access or modify class static & generally for utility.

# class Student:
#     @classmethod
#     def college(cls):
#         pass


class Person:
    name = "Anonymous"

    # def changename(self, name):
    #     # self.name = name
    #     self.__class__.name = name
    #     # Person.name = name

    @classmethod
    def changename(self, name):
        self.name = name

p1 = Person()
p1.changename("Abhishek Maurya")
print(p1.name)
print(Person.name)
