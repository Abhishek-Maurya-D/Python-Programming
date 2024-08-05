# WAP to find the greatest of 3 numbers entered by the user

num1 = int(input("Enter the 1st Number : "))
num2 = int(input("Enter the 2nd Number : "))
num3 = int(input("Enter the 3rd Number : "))

if(num1>=num2 and num1>=num3):
    print(num1, "is the greatest one.")
elif(num2>=num1 and num2>=num3):
    print(num2, "is the greatest one.")
else:
    print(num3, "is the greatest one.")
