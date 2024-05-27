# Nesting Statements

age = int(input("Enter the age : "))
if(age>=18):
    if(age>=80):
        print("Can't Drive")
    else:
        print("Can Drive")
else:
    print("Can't Drive")