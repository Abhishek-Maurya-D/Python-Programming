# Dictionary Methods

student = {
    "name" : "Abhishek Maurya",
    "subject" : {
        "phy" : 76,
        "chem":92,
        "math" :85
        }
}

# print(student.keys()) # returns the key values of the dictionary
# print(list(student.keys())) # creation of list by key value pairs
# print(len(student)) # number of key values
# print(len(student.keys())) # number of key values
# print(len(list(student.keys()))) # number of key values

# print(student.values()) # for printing the values of the keys
# print(list(student.values()))

# print(student.items()) # returns the key value pairs in the form of tuples
# print(list(student.items()))

# pairs = list(student.items())
# print(pairs[0])

# print(student.get("name")) # returns the key according to value
# print(student["name"])

# print(student.get("name2")) # No error --> None
# print(student["name2"]) # error
# print("hi")
# print("Welcome")
# print("Abhishek Maurya")
# print("Done")

# student.update({"City":"Delhi"}) # inserts the specified items to the dictionary
# print(student)

new_dict = {"City":"Delhi", "name":"Ankur Yadav"}
student.update(new_dict) # inserts the specified items to the dictionary
print(student)