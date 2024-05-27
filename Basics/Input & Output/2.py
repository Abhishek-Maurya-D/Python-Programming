# Predicting the output

# consider the given expression : not True and False or True
# which of the following will be correct output if the given expression is evaluated?
# 1. True 2. False 3. None 4. Null

# Now the evaluation is 
# not True and False or True
# (not True) and False or True
# (False and False) or True
# False or True
# True
# so, answer is true

x = not True and False or True
print(x)