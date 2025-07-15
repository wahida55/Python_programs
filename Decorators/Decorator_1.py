#Decorators take an input function as argument and return an output function with
#some extended functionality.

# Syntax:
# def decorator_function(input function):
#     def output function():
#         add extra functionality
#     return output function
'''A decorator is a function that takes another function as input and returns a new function
with added functionality
Syntax :
def decorator_function(Original_function):
    def wrapper_function():
        print("Something before the original function")
        original_function()
        print("Something after original function")
    return wrapper_function'''
def decor(func):
    def inner():
        print("Added extended functionality")
    return inner
@decor
def display():
    print("Function as it is")
display()



