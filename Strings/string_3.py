#WAP to merge the characters from two strings into a single string by taking characters alternatively
#if same length string :

'''
s1=input("Enter first string :")
s2=input("Enter second string :")
i,j=0,0
output= ''
while i<len(s1) or j<len(s2):
    output=output + s1[i]+s2[j]
    i+=1
    j+=1
print(output)
'''
#if different length string :
s1=input("Enter first string :")
s2=input("Enter second string :")
i,j=0,0
output= ''
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output + s1[i]
        i+=1
    if j<len(s2):
        output=output + s2[j]
        j+=1
print(output)
