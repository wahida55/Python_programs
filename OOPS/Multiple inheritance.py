#Multiple inheritance has multiple base class and one derived class.
#
class Father:
    def __init__(self):
        print("Hello , I am father!")
    def childcare(self):
        print("I need to provide for my child!(Father)")
class Mother():
    def __init__(self):
        print("Hello, I am mother ")
    def childcare(self):
        print("I need to provide for my child!(Mother)")
class child(Father,Mother):
    def __init__(self):
        print("Hello, I am child ")
        super().__init__()
c = child()
