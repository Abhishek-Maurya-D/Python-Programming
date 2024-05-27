# Dictionary are used to store data values in key:value pairs
# They are unordered, mutable(changedable) & don't allow duplicate keys

info = {
    "name" : "Abhishek Maurya",
    "Subject" : ["Python", "C", "C++"],
    "learining" : "Coding",
    "age" : 43,
    34.34 : 34.445,
    (434,34,34,34) : (234,234,234,234,234,454)
}

print(info["name"])
# key values can be tuple, string, float values
info["name"] = "apna college"
print(info)
print(type(info))

print()
null_dict = {}
print(type(null_dict))
print(null_dict)