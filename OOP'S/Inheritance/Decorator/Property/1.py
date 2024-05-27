# Property
# We use @property decorator on any method in the class to use the method as a property.

class student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    def calcpercentage(self):
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

stu1 = student(92,85,76)
print(stu1.percentage)

stu1.phy = 82
print(stu1.phy)
stu1.calcpercentage()
print(stu1.percentage)