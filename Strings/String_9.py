#Count each character in string using count
s=input("Enter any string :")
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
for ch in sorted(l):
    print("{} occurs {} times".format(ch,s.count(ch)))

    
