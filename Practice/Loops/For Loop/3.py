# WAP to find the sum of first n numbers.

num = int(input("Enter the Number : "))
sum = 0
for el in range(num+1):
    sum += el
print("Sum of all the Number is :", sum)