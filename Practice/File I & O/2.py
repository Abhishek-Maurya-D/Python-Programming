# WAF that replace all occurrences of "Java" with "Python" in the file 1.py

f = open("C:/Users/Abhishek/OneDrive/Desktop/Python/Practice/File I & O/practice.txt", "r")
data = f.read()
f.close()

new_data = data.replace("Java", "Python")
print(new_data)

f = open("C:/Users/Abhishek/OneDrive/Desktop/Python/Practice/File I & O/practice.txt", "w")
f.write(new_data)
f.close