sen = "This is a string where I need to find the no of vowels occurring."
vowels = "aeiou"
v=[]
for ch in sen:
    if ch.casefold() in vowels :
        v.append(ch)
print(v)
print(len(v))



