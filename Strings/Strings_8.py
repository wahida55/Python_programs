#program to remove duplicates from a string
s=input("Enter any string:")
output =''
for ch in s:
    if ch not in output:
        output=output+ch
print(output)