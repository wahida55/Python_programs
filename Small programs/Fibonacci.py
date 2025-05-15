n1,n2=0,1
count = 0
n=int(input("Enter the number :"))
if n==1:
    print("Fibonacci series for 1th term is :",n1)
print("Fibonacci series:",end="\n")
while count<n:
    print(n1)
    nth=n1+n2
    n1=n2
    n2 = nth
    count+=1
