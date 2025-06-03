n=input("Enter number :")
try :
    for i in range(1,11):
        print(int(n)*i)
except :
    print("invalid input")
finally :
    print("finally code ")