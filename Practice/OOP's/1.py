# Create student class takes name & marks of 3 subjects as arguments in constructor. 
# Then create a method to print the average

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self, marks):
        sum = 0
        for val in marks:
            sum += val
        print("Hi", self.name, "you avg score is : ", sum/3)

s1 = Student("Abhishek Maurya", [85,92,76])
s1.get_avg(s1.marks)