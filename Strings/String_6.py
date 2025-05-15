#WAP for req input a3z2b4 and output aaabbbzzz
s=input("Enter any string :")
output = ''
for ch in s:
    if ch.isalpha():
        x=ch
    else :
        d=int(ch)
        output=output+x*d
ls=list(output)
print(''.join(sorted(ls)))


