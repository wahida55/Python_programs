#WAP to sort characters of a string, first alphabets then digits.
from Programs.String_2 import output

s=input("Enter any string :")
alpha=[]
dig=[]
for ch in s:
    if ch.isalpha():
        alpha.append(ch)
    if ch.isdigit():
        dig.append(ch)
output=sorted(alpha)+sorted(dig)
print(output)
ls=''.join(output)
print(ls)