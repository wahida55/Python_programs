count = 0
vowels="aeiouAEIOU"
str=input("Enter any string:")
for ch in str:
    if ch in vowels:
        count+=1
print("No of vowels =",count)