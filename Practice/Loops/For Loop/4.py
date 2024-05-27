# WAP to find the factorail of a numbers n.

num = int(input("Enter the Number to calculate the factorial: "))
fact = 1
for el in range(1,num+1):
    fact *= el
print("Factorial of ",num," is ",fact)