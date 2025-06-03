string = input("Enter any string")
i = len(string)-1
output = ""
while i >= 0:
    output = output + string[i]
    i-=1
print(output)