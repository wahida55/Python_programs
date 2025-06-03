string = input("Enter any string")
vowels = "aeiou"
v=""
consonants = ""
for ch in string :
    if ch.casefold() in vowels:
        v=v+ch
    else :
        consonants=consonants+ch
print(v)
print(consonants)