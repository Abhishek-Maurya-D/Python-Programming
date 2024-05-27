# Set Method
collection = set()
collection.add(1) # set.add(el) # adds an element
collection.add(2)
collection.add(2)
# collection.remove(7)  # 7 is not in the list
collection.add("Abhishek Maurya")
collection.add((1,2,3))
# collection.add([1,2,3]) 
print(len(collection))
print(collection)
collection.remove("Abhishek Maurya") # set.remove(el) # removes the element
print(collection)
collection.clear() # set.clear() # empties the set
print(collection)



collection1 = {"Hello", "World", "python","Abhishek"}
print(collection1.pop()) # set.pop() # removes a random value
print(collection1.pop())

# set.union(set2) # combines both set values & return new
# set.intersetion(set2) # combines common values & return new

set2 = {1,2,3}
set3 = {3,5,4}
print()
print(set2.union(set3))
print(set3.intersection(set2))