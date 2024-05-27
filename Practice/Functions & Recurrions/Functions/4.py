# WAP to convert USD to INR

num = int(input("Enter the Money in USD: "))

def convert_curr(usd):
    rup = usd*82
    print("Money in Rupee is: ", rup)

convert_curr(num)