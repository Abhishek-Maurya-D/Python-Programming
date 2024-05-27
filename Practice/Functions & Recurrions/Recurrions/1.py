# Write a recursive function to calculate the sum of first n natural numbers.

num = int(input("Enter the Number ; "))

sum = 0
def sum_nat(no):
    if(no==1):
        return 1
    return  (no + sum_nat(no-1))
    
print(sum_nat(num))