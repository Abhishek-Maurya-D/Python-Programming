# WAP  to print the elements of a list in a single line.<list is the parameter>

city = ["mumbai", "Delhi", "Noida", "Chennai", "kolkata"]

def print_ele(list):
    for el in list:
        print(el, end = " ")

print_ele(city)