# String & Numeric values can  operate together with *

A, B = 2,3
Txt = "@"
print(2*Txt*3)

# String & String can operate with +
# Concatination

A, B = "2", 3
Txt = "@"
print((A+Txt)*B)

# Numeric values can operate with all arithmetic operators

A, B = 2, 3
C = 4
print(A+B*C)


#Arithmetic expression with integer and float will result in float

A, B = 10, 5.0
C = A*B
print(C)

# Result of division operator with two integers will be float

A, B = 1, 2
C = A/B
print(C)

#Integer division with float and int will give int display as float 
# sign for integer division is //
a, b = 1.5, 3
c = a//b
print(c, a/b)