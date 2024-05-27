# Break : used to terminate the loop when encountered.
# Continue : terminates exection in the current iteration & continues exection of the loop with the next StopIteration

i = 1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1