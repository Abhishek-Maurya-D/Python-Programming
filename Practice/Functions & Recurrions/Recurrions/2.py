# Write a recursive function to print all elements in a list.append
# Hint: use list & index as parameter

list = ["Abhishek", "Himanshu", "Rohit", "Ankit", "Ankur"]

def print_ele(list, num):
    num-=1
    if(num==-1):
        return
    print_ele(list, num)
    print(list[num])

print_ele(list, len(list))