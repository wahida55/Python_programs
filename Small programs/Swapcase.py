str = "This is a String in Python"
# str_upper = str.swapcase()
# print(str_upper)
st = ""
for ch in str:
    if ch.isupper():
        st = st + ch.lower()
    else :
        st = st + ch
print(st)