'''
i=1
while i <=100:
    print(i)
    i+=1
'''
'''
i = 100
while i >= 1 :
    print(i,end=" ")
    i-=1
'''
'''
i = 1
n=int(input("Enter any number : "))
while i<=10 :
    print(n*i)
    i+=1
'''
'''
list =[1,4,9,16,25,36,49,64,81,100]
index = 0
l=len(list)
while index<l:
    print(list[index])
    index+=1
'''
'''
tup = (1,4,9,16,25,36,49,64,81,100)
n=int(input("Enter element to search :"))
index = 0
l=len(tup)
while index < l:
    if(tup[index]==n):
        print("Element found at index :",index)
    index+=1
'''
'''
n=int(input("Enter any number :"))
for i in range(1,11):
    print(n*i)
'''
'''
n=int(input("Enter any number :"))
sum = 0
for i in range(1,n+1):
    sum=sum+i
print(sum)
'''
n=int(input("Enter any number :"))
fact = 1
for i in range(1,n+1):
    fact = fact*i   
print(fact)