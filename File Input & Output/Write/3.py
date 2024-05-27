# it will add the content in the file and during this 
# process the pointer is at the starting of the file

# in "r+" mode both reading and writing both occurs


# f = open("C:/Users/Abhishek/OneDrive/Desktop/Python/File Input & Output/Write/2.txt", "r+")
# f.write("Abh")
# print(f.read())
# f.close()

# in "w+" we will write and read the file 
# first write and then read the content of the file

# f = open("C:/Users/Abhishek/OneDrive/Desktop/Python/File Input & Output/Write/2.txt", "w+")
# # f.write("Abh")
# f.write("ABhishek maurya")
# print(f.read())
# f.close()

# in "a+" mode 

f = open("C:/Users/Abhishek/OneDrive/Desktop/Python/File Input & Output/Write/2.txt", "a+")
# f.write("Abh")
print(f.read())
f.write("ABhishek maurya")
f.close()