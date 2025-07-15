s = input("Enter any string to check palindrome :")
s = s.replace(" ","").lower()
if s == s[::-1]:
    print("It is a PALINDROME")
else :
    print("Not a palindrome !")