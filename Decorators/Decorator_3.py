def decor_wish(func):
    def inner(name):
        if name == "Sunny":
            print("*"*30)
            print("Welcome Sunny!!")
            print("*" * 30)
        else :
            func(name)
    return inner
@decor_wish
def decor_name(name):
    print("Welcome to the lecture "+name)
decor_name("Sunny")
decor_name("Bunny")

