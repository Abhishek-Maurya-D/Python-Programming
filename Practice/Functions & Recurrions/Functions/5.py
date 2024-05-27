# WAP to check the entered number is odd or even

num = int(input("Enter the Number : "))

def num_check(no):
    if(no%2==0):
        print("Even")
    else:
        print("Odd")

num_check(num)