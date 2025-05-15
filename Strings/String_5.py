#WAP for requirement a4b3c2 and expected aaaabbbcc
s=input("Enter the string : ")
output=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        output=output+x*d
print(output)