# WAP to enter marks of 3 subjects from the user and store 
# them in a dictionary. Start with an empty dictionary & 
# add one by one. Use subject name as key & marks as value.

marks = {}
x = int(input("Enter the marks of Physics: "))
marks.update({"Physics" : x})
x = int(input("Enter the marks of Maths: "))
marks.update({"Maths" : x})
x = int(input("Enter the marks of Chemistry: "))
marks.update({"Chemistry" : x})

print(marks)