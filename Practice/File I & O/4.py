# WAP to find in which line of the file does the word "learing" occurs first.
# print - 1 if word not found

def check_for_line():
    word = "learing"
    data = True
    line_no = 1
    with open("C:/Users/Abhishek/OneDrive/Desktop/Python/Practice/File I & O/practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

check_for_line()