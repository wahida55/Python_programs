# tell() tells us where the cursor is present in the file from the beginning of file.
# seek() move cursor to the particular position.
f = open("New_text","r")
print(f.tell())
print(f.read(5))
print(f.tell())
print(f.seek(2))
print(f.tell())

f.close()
