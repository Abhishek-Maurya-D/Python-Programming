# WAP to check if a list contains a palindrome of elements.

list1 = [1,2,3,2,1]
list2 = [2,3,4,5]

copy_list1 = list1.copy()
copy_list1.reverse()
copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list1 == list1):
    print("List1 is Palindrome")
else:
    print("List1 is not a Palindrome")
print()
if(copy_list2 == list2):
    print("List2 is Palindrome")
else:
    print("List2 is not a Palindrome")