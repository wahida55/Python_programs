#Single parent and single child
class Parent:
    def __init__(self):
        print("Welcome to parent class")
class Child(Parent):
    def __init__(self):
        print("Welcome to child class")
        super().__init__() #invokes parent class methods in case they have the same method name
CC = Child()
