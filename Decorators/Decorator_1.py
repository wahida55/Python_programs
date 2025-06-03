#Decorators take an input function as argument and return an output function with
#some extended functionality.

# Syntax:
# def decorator_function(input function):
#     def output function():
#         add extra functionality
#     return output function

def decor(func):
    def inner():
        print("Added extended functionality")
    return inner
@decor
def display():
    print("Function as it is")
display()