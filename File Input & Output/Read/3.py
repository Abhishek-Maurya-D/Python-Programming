# Reading a File

# data = f.read() # reads entire file
# data = f.readline() reads one line at a Time


# pass_file = open("C:/Users/Abhishek/OneDrive/Desktop/All password 1.docx","rt")
# data = pass_file.read()
# print(data)
# pass_file.close()

from docx import Document

doc = Document("C:/Users/Abhishek/OneDrive/Desktop/cover letter.docx")
data = "\n".join([para.text for para in doc.paragraphs])
print(data)
