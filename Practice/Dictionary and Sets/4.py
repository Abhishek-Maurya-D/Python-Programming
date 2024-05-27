# Figure out a way to store 9 & 9.0 as separate values in
# set. (You can take help of built-in data type)

set = {9, "9.0"}
print(set)

set1 = {
    ("float", 9.0),
    ("int", 9)
}
print(set1)