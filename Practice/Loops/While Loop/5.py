# search for a number x in this tuple using loops
# (1,4,9,16,25,36,49,64,81,100)

tuple = (1,4,9,16,25,36,49,64,81,100)
num = int(input("Enter the Number : "))
i=0
while i<len(tuple):
    if num == tuple[i]:
        print("Number is found at index", i)
        break
    else:
        print("Finding...")
    i+=1