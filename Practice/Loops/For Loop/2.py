# search for a number x in this tuple using loop
# (1,4,9,16,25,36,49,64,81,100)

num = int(input("Enter the Number : "))
list = (1,4,9,16,25,36,49,64,81,100)
idx = 0
for el in list:
    idx+=1
    if(num == el):
        print("Number is found at index : ",idx)
        break
    else:
        print("Finding..")
else:
    print("Number don't exist")