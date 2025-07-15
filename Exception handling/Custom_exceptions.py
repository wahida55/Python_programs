class NotInRange(Exception):
    "raised when number not in range"
    pass
n = int(input("Enter number between 5 & 10 :"))
if n>=5 and n<=10:
    print("Nice number !")
else:
    raise NotInRange("Value should be in between 5 and 10")
#except NotInRange:

