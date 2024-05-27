# when a funtion calls itself repeatedly.

# Recursion == Loops

# reverse number printing
num = int(input("Enter the Number : "))

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(num)