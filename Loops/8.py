# range function
# Range functions returns a sequence of numbers, starting
# from 0 by default, and increments by 1(by default), and
# stops before a specified number.

# Syntax
# range(start?, stop, step?)
# by default start and step = 1

list = [1,3,4,5,5,7,8,5,3,1,6]

for el in range(5):
    print(el)

for el in range(1,5):
    print(el)

for el in range(1, 5, 2):
    print(el)