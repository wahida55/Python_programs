#Hierarchical level inheritance one parent and multiple children
class Parent:
    def __init__(self):
        print("Hello , I am parent!")
class son(Parent):
    def __init__(self):
        print("Hello, I am son ")
        super().__init__()
class daughter(Parent):
    def __init__(self):
        print("Hello, I am daughter ")
        super().__init__()
d = daughter()
s = son()
