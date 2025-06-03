def decor_add(func):
    def inner(a,b):
        print("#"*30)
        print("The sum is :",end = "")
        func(a,b)
        print("#"*30)
    return inner
@decor_add
def add(a,b):
    print(a+b)
add(10,20)

