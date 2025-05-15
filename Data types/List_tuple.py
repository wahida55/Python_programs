# ===============LISTS=====================
# Ordered,mutable,indexed.
# Allows duplicates.
#Practicing GIT comments.
# Built in data type to store elements of different types.
"Lists methods return none unlike string methods which return the updated string"

list = [3, 4, 6, 3, 5, 8, 9, 0, 10, 34, 23]
print(list)
list.sort()  # Sorts the list in ascending order
print(list)
list.sort(reverse=True)  # Sorts is descending order
print(list)
list.reverse()  # reverses the list
print(list)
list.insert(6, 3)  # inserts elements at index
print(list)
list.remove(4)  # removes element "4"
print(list)
list.pop(2)  # removes element at index 2
print(list)


# ===============TUPLES=====================

# Built in data types to create immutable sequence of values.
# No item assignment.
# ordered and unchangeable. Allows duplicate members.

tup = (1, 3, 2, 5, 6, 3)
print(tup)
print(tup.index(3)) # returns the index of 3
print(tup.count(3)) # returns the occurence of 3