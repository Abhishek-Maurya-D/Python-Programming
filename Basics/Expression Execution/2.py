# Expression Execution
# floor gives closest integer, which is lesser than or equal to the float value
# Result of (A // B) is same as floor (A/B)

a, b = 12, 5
c = a//b
print(c)

a, b = -12, 5
c = a//b
print(c)

a, b = 12, -5
c = a//b
print(c)