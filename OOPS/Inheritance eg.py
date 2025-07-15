class A:
    @staticmethod
    def gparent():
        print("I am grandparent")

    def human(self):
        print("I am a human being from gparent class")
class B(A):
    @staticmethod
    def parent():
        print("I am a parent ")

    def human(self):
        print("I am a human being from parent class")
class C(B):
    @staticmethod
    def child():
        print("I am the child")

    def human(self):
        print("I am a human being from child class")
        super().human()
person = C()
person.human()
