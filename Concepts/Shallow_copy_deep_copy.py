#A shallow copy creates a new object which stores the reference of the original elements.
#A deep copy creates a new object and recursively adds the copies of nested objects present in
# the original elements.

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)

# OUTPUT
# Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
# New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)



