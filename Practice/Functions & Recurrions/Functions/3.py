# WAP to find the factorial of n. (n is the parameter)

num = int(input("Enter the Number to calculate the Factorial : "))

def fun_fact(el):
    fact=1
    for i in range(1,el+1):
        fact *=i
    print("Factorial of Number is : ", fact)

fun_fact(num)