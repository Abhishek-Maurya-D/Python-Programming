# Class and Instance Attributes
# Class.attr
# obj.attr

class Student:
    college_name = "IIMT College of Engineering"
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks 
        print("Adding new Student in Database..")

s1 = Student("Abhishek Maurya", 87)
print(s1.name, s1.marks)

s2 = Student("Abhimanyu Maurya", 92)
print(s2.name, s2.marks)

print(Student.college_name)