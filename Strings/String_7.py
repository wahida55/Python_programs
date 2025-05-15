#WAP input:aaaabbbzzz,output:4a3b1z
s=input("Enter the string :")
output =''
previous=s[0]
i=1
c=1
n=len(s)
while i<n:
    if s[i]==previous:
        c+=1
    else:
        output=output+str(c)+previous
        c=1
        previous=s[i]
    if i==n-1:
        output=output+str(c)+previous
    i+=1
print(output)
