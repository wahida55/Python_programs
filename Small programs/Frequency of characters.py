Str = "This is a string. lets count the characters!"
for i in Str:
    freq = Str.count(i)
    print(f"Character {i} occurs {freq} times")

# Using a dictionary

Str = "This is a string. lets count the characters!"
dict = {}
for i in Str:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)

from collections import Counter
string = "Yolo Life"

output = Counter(string)

print(output)