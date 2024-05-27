# WAP to find the sum of first n numbers.

num = int(input("Enter the Number : "))
sum = 0
i = 1
while i<=num:
    sum += i
    i+=1
print("Sum of all the Number is :", sum)