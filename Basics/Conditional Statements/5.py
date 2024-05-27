#clever if | Ternary operator
# <var> = (false_val, true_val) [<Condition>]

age = int(input("Age : "))
vote = ("Yes", "No") [age>=18]

sal = float(input("Salary : "))
tax = sal*(0.1, 0.2) [sal>50000]
print(tax)