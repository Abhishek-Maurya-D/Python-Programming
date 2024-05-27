class Student:

    #default constructors
    def __init__(self):
        pass

    # Parameterized Constructors
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks 
        print("Adding new Student in Database..")

s1 = Student("Abhishek Maurya", 87)
print(s1.name, s1.marks)

s2 = Student("Abhimanyu Maurya", 92)
print(s2.name, s2.marks)