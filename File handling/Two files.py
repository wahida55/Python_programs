f1 = open("New_text","r")
f2 = open("Second_file","r+")
data = f1.read()
write_data = f2.write(data)
print(f2.read())
f1.close()
f2.close()