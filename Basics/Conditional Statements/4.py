#Single Line if/ Ternary operator
# <var> = <val1> if <condition> else <var2>

food = input("Food : ")
eat = "Yes" if food == "cake" else "no"
print(eat)

# <str1> if <condition> else <str2>
food = input("Food : ")
print("Sweet") if food == "cake" or food == "jalebi" else print("not sweet")