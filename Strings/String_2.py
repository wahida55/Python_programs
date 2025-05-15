#WAP to reverse internal content of every second letter of a string

s=input("Enter any string :")
l1=s.split()
l2=[]
print(len(l1))
i=0
while i<len(l1):
    if i%2==0:
        l2.append(l1[i])
    else:
        l2.append(l1[i][::-1])
    i+=1
output=' '.join(l2)
print(output)

