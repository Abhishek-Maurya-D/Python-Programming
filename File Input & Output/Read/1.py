# File I/O in Python 
# Python can be used to perform operations on a file.

# types of files 
# 1. Text file - .txt, .docx, .log, etc.
# 2. Binary file - .mp4, .mov, .png, .jpeg, etc


f = open("C:/Users/Abhishek/OneDrive/Desktop/Python/File Input & Output/1.txt", "rt")
data = f.read()
print(data)
print(type(data))
f.close()
