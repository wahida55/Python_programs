#WAP to reverse the internal contents of each word

s=input("Enter any string :")
l=s.split()
l1=[]
for word in l:
    l1.append(word[::-1])
print(l1)
ls=' '.join(l1)
print(ls)


