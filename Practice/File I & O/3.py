# Search if the word "learing" exists in the file or not.


word = "learing"
with open("C:/Users/Abhishek/OneDrive/Desktop/Python/Practice/File I & O/practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not found")