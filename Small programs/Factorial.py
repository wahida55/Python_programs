# def factorial(n):
#     if n==0 or n==1 :
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))


def facto(num):
    fact = 1
    if num == 0 or num == 1:
        print("Factorial is 1!")
    for i in range(2,num+1):
        fact=fact * i
    print(fact)
facto(1)
