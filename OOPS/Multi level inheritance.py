#Multi level inheritance has levels in inheritance
class grandParent:
    def __init__(self):
        print("Hello , I am grandparent!")
class parent(grandParent):
    def __init__(self):
        print("Hello, I am parent ")
        super().__init__()
class child(parent):
    def __init__(self):
        print("Hello, I am child ")
        super().__init__()
CC = child()
