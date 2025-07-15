# WAP to check whether a list contains a palindrome of elements.

list1 = [1, 2, 3, "Banana", "cherry", 3, 2, 1]
print(list1)
list2 = list1.copy()
list2.reverse()
print(list2)
if list1 == list2:
    print("List is palindrome")
else:
    print("List is not a palindrome")
