num=int(input("Enter any number to check :"))
sum=0
temp=num
while temp>0:
    dig=temp%10
    sum=sum+dig**3
    temp//=10
if num==sum:
    print("{} is an armstrong number".format(num))
else:
    print("{} is not an armstrong number".format(num))